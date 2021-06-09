"""
Author: Jose Stovall | oitsjustjose
"""

import argparse
import sys

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
        "-r",
        "--root",
        help="The root on your disk for THIS server",
        required=True,
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="The seed to use for the world",
        required=False,
    )

    parser.add_argument(
        "-l",
        "--leveltype",
        help="The level type to use for the world",
        required=False,
    )

    ########################################################
    #       Less common commands, with no shortcuts        #
    ########################################################

    parser.add_argument(
        "--view",
        help="The view distance the server should run at",
        required=False,
    )

    parser.add_argument(
        "--motd",
        help="The MOTD for the server",
        required=False,
    )

    parser.add_argument(
        "--memory",
        help="The amount of dedicated memory for the server",
        required=False,
    )

    parser.add_argument(
        "--aikar",
        help="If flag is included, loads the server using aikar's flags",
        action="store_true",
        required=False,
    )

    parser.add_argument(
        "--java",
        help="Allows you to specify the java version",
        choices=['8', '11', '16'],
        default=16,
        required=False,
    )

    parser.add_argument(
        "--forge",
        help="Allows you to provide either a URL or Path to a Forge installer",
        required=False,
    )

    parser.add_argument(
        "--fabric",
        help="Allows you to provide either a URL or Path to a Fabric installer",
        required=False,
    )

    parser.add_argument(
        "--modpack",
        help="Allows you to specify a CURSEFORGE modpack",
        required=False,
    )

    parser.add_argument(
        "--players",
        help="Allows you to specify the max player count",
        required=False,
    )
