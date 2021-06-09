"""
Author: Jose Stovall | oitsjustjose
"""
# pylint: disable=broad-except, bare-except

import os
from typing import Union

import docker

from logger import Logger


class DockerManager:
    """
    A Management system for a docker container
    """

    def __init__(self, name):
        self._name = name
        self._client = docker.from_env()
        self._container = self._get_container()
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

    def create_server(
        self, version: str, port: Union[int, str], root: str, motd="", maxr="2G"
    ):
        """
        Creates a new docker container
        """
        try:
            if os.path.exists(root):
                self._log.warn(f"Server root '{root}' exists - there may be problems!")
            self._client.containers.run(
                "itzg/minecraft-server",
                name=self._name,
                ports={25565: port},
                environment={
                    "VERSION": version,
                    "EULA": True,
                    "MOTD": motd,
                    "MEMORY": maxr,
                },
                volumes={root: {"bind": "/data", "mode": "rw"}},
                detach=True,
            )
            self._container = self._get_container()
            self._log.success("Successfully Created Server")

        except Exception as exception:
            self._log.err("Failed to Create Server")
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
