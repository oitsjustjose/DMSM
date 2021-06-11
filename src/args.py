"""
Author: Jose Stovall | oitsjustjose
"""

import argparse
import sys

from constants import SERVER_ENVS
from logger import Logger


def get_args() -> argparse.Namespace:
    """
    Cleanly and with education gets the arguments for the program
        Does so based on the current task given, if any
        Throws errors and a tantrum if you don't give it candy
        Please give it candy 🍬
    Arguments:
        None
    Returns:
        (argparse.NameSpace) the arguments for the program
    """
    parser = argparse.ArgumentParser(
        description="Arguments for Docker Minecraft Server Management (DMSM)",
        add_help=False,
    )

    if len(sys.argv) >= 2 and sys.argv[1] == "create":
        _create(parser)

    if len(sys.argv) >= 2 and sys.argv[1] in ["stop", "restart"]:
        _stop_restart(parser)

    if not _validate(parser):
        sys.exit(1)

    return parser.parse_args(args=sys.argv[3:])


def _validate(parser: argparse.ArgumentParser) -> bool:
    if len(sys.argv) < 3:
        logger = Logger()
        logger.err("This utility requires at least the following:")
        logger.info(
            f"\t{sys.argv[0]} (create|start|stop|restart|delete) SERVERNAME [options]"
        )
        parser.print_help()
        return False
    return True


def _stop_restart(parser: argparse.ArgumentParser):
    """
    Handles adding the stop/restart arguments
    """
    parser.add_argument(
        "-f",
        "--force",
        help="Will forcibly shut down the server",
        action="store_true",
        required=False,
    )


def _create(parser: argparse.ArgumentParser):
    """
    Handles adding the create arguments
    """

    ########################################################
    #  Below are the more common commands, with shortcuts  #
    ########################################################

    required = parser.add_argument_group("Required Arguments")
    optional = parser.add_argument_group(
        "Optional Arguments (oitsjustjo.se/u/Z9mLwAY40)"
    )

    required.add_argument(
        "-p",
        "--port",
        help="The port to run the newly created server on",
        default="25565",
        required=True,
    )

    required.add_argument(
        "-v",
        "--version",
        help="The version of Minecraft to run",
        required=True,
    )

    required.add_argument(
        "-r",
        "--root",
        help="The root on your disk for THIS server",
        required=True,
    )

    optional.add_argument(
        "-j",
        "--java",
        help="Allows you to specify the java version",
        choices=["8", "11", "16"],
        default=16,
        required=False,
    )

    for env in SERVER_ENVS.keys():
        optional.add_argument(
            f"--{env}",
            required=False,
            type=SERVER_ENVS[env],
        )
