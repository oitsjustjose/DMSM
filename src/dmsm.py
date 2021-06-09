"""
Author: Jose Stovall | oitsjustjose
"""

import argparse
import sys

from docker_mgr import ServerManager
from logger import Logger


def get_args() -> argparse.Namespace:
    """
    Cleanly and with education gets the arguments for the program
        Does so based on the current task given, if any
        Throws errors and a tantrum if you don't give it candy
        Please give it candy.
    Arguments:
        None
    Returns:
        (argparse.NameSpace) the arguments for the program
    """
    parser = argparse.ArgumentParser(
        description="Arguments for Docker Minecraft Server Management (DMSM)",
    )

    if len(sys.argv) >= 2 and sys.argv[1] == "create":
        parser.add_argument(
            "-p",
            "--port",
            help="The port to run the newly created server on",
            default="25565",
            required=True,
        )
        parser.add_argument(
            "-v",
            "--version",
            help="The version of Minecraft to run",
            required=True,
        )
        parser.add_argument(
            "--root",
            "-r",
            help="The root on your disk for THIS server",
            required=True,
        )
        parser.add_argument(
            "--motd",
            help="The MOTD for the server",
            required=False,
            default="A Minecraft Server",
        )
        parser.add_argument(
            "-m",
            "--memory",
            help="The amount of dedicated memory for the server",
            default="2G",
            required=False,
        )

    if len(sys.argv) >= 2 and sys.argv[1] in ["stop", "restart"]:
        parser.add_argument(
            "-f",
            "--force",
            help="Will forcibly shut down the server",
            action="store_true",
        )

    if len(sys.argv) < 3:
        logger = Logger()
        logger.err("This utility requires at least the following:")
        logger.info(
            f"\t{sys.argv[0]} (create|start|stop|restart|delete) SERVERNAME [options]"
        )
        parser.print_help()
        sys.exit(0)

    return parser.parse_args(args=sys.argv[3:])


def main(args: argparse.Namespace) -> None:
    """
    The main program function
    Arguments:
        args (NameSpace): the program's args
    """

    action = sys.argv[1]
    server_name = sys.argv[2]
    mgr = ServerManager(server_name)

    if action == "create":
        mgr.create_server(args)
    elif action == "start":
        mgr.start_server()
    elif action == "stop":
        mgr.stop_server(force=args.force)
    elif action == "restart":
        mgr.restart_server(force=args.force)
    elif action == "delete":
        mgr.delete_server()
    elif action == "status":
        mgr.get_status()
    elif action == "console":
        mgr.open_console()


if __name__ == "__main__":
    main(get_args())
