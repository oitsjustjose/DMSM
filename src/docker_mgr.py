"""
Author: Jose Stovall | oitsjustjose
"""
# pylint: disable=broad-except, bare-except

import os
import subprocess
from argparse import Namespace
from typing import Dict

import docker
from constants import SERVER_ENVS

from logger import Logger


def _build_env(args: Namespace) -> Dict[str, any]:
    """
    This function builds an Environment dict that can be
    directly passed into the docker container creation

    Arguments:
        args (Namespace): The CLI args
    Return:
        (Dict[str, any]): the args, dictified
    """
    ret = {"VERSION": args.version, "EULA": True}
    for arg in vars(args):
        if getattr(args, arg):
            if arg in SERVER_ENVS.keys():
                ret[arg.upper()] = getattr(args, arg)

    return ret


class ServerManager:
    """
    A Management system for a docker container
    """

    def __init__(self, name):
        self._name = name
        self._client = docker.from_env()
        self._container = self._get_container()
        self._backup_container = None
        self._log = Logger(name=self._name)

    def _get_container(self):
        for container in self._client.containers.list(all=True):
            if container.name == self._name:
                return container
        return None

    def get_docker_client(self):
        """
        Gets the Docker Client Instance
        """
        return self._client

    def create_server(self, args: Namespace):
        """
        Creates a new docker container
        """
        try:
            if os.path.exists(args.root):
                self._log.warn(
                    f"Server root '{args.root}' exists - there may be problems!"
                )
            self._client.containers.run(
                f"itzg/minecraft-server:java{args.java}",
                name=self._name,
                ports={25565: args.port},
                environment=_build_env(args),
                volumes={args.root: {"bind": "/data", "mode": "rw"}},
                detach=True,
            )
            self._container = self._get_container()
            self._log.success("Successfully Created Server")

            if args.backup:
                self._start_backup_cont(args)

        except Exception as exception:
            self._log.err("Failed to Create Server")
            self._log.err(exception)

    def _start_backup_cont(self, args: Namespace):
        """
        Creates a container for the backup service
        """
        try:
            self._client.containers.run(
                "itzg/mc-backup",
                name=f"{self._name}-Backup",
                environment={"INITIAL_DELAY": "0m", "BACKUP_INTERVAL": "30m"},
                volumes={
                    args.root: {"bind": "/data", "mode": "ro"},
                    args.backup: {"bind": "/backups", "mode": "rw"},
                },
                network=f"container:{self._name}",
                detach=True,
            )
            self._log.success("Successfully Started Backups")
        except Exception as exception:
            self._log.err("Failed to Create Backup Service for Server")
            self._log.err(exception)

    def delete_server(self):
        """
        Deletes a docker container
        """
        try:
            self.stop_server(force=True)
            self._container.remove()
            self._log.success("Successfully Deleted Server")
        except:
            self._log.err("Failed to Delete Server")

    def start_server(self):
        """
        Starts a docker container
        """
        if self._container and self._container.status == "running":
            self._log.warn("Server Already Running")
        else:
            self._container.start()
            self._container = self._get_container()
            self._log.success("Successfully Started Server")

    def stop_server(self, force=False):
        """
        Stops a docker container
        """
        try:
            if force:
                self._container.kill()
            else:
                self._container.stop()
            self._log.success("Successfully Stopped Server")
        except:
            self._log.err("Failed to Stop Server")

    def restart_server(self, force=False):
        """
        Restarts a docker container
        """
        try:
            if force:
                self._container.kill()
                self._container.start()
            else:
                self._container.restart()
            self._log.success("Successfully Restarted Server")
        except:
            self._log.err("Failed to Restart Server")

    def get_status(self):
        """
        Gets the status of a contianer
        """
        health = str(
            subprocess.check_output(
                [
                    "docker",
                    "container",
                    "inspect",
                    "-f",
                    "{{ .State.Health.Status }}",
                    self._name,
                ]
            )
            .decode()
            .replace("\n", "")
        )
        container_status: str = self._container.status

        if container_status.lower() == "running":
            if health.lower() == "healthy":
                self._log.success("Server is running and healthy")
            elif health.lower() == "starting":
                self._log.notice("Server is starting")
            else:
                self._log.warn(f"Server is running but in degraded state: {health}")
        else:
            self._log.info(f"Server is {self._container.status}")

    def open_console(self):
        """
        Connects the user to the server's console
        """
        os.system(f"docker exec -i {self._name} rcon-cli")
