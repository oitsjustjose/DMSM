"""
Author: Jose Stovall | oitsjustjose
"""

import argparse
import sys

from constants import SERVER_ENVS


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
    parser = argparse.ArgumentParser(description="Arguments for DMSM", add_help=False)

    positional = parser.add_argument_group("Positional Arguments")
    positional.add_argument(
        "servername",
        nargs=1,
        type=str,
    )
    positional.add_argument(
        "task",
        choices=[
            "create",
            "start",
            "stop",
            "restart",
            "delete",
            "status",
            "console",
            "logs",
            "help",
            "?",
        ],
        nargs=1,
        type=str,
    )

    # If the user performs dmsm <SERVER_NAME> create:
    if len(sys.argv) >= 3 and sys.argv[2] == "create":
        _create(parser)

    if len(sys.argv) >= 3 and sys.argv[2] in ["stop", "restart"]:
        parser.add_argument(
            "-f",
            "--force",
            help="Forces the Minecraft server to shut down",
            required=False,
            action="store_true",
        )

    if len(sys.argv) >= 2:
        # If the user performs dmsm ? or dmsm help
        if "help" in sys.argv[1].lower() or "?" in sys.argv[1].lower():
            _create(parser)
            parser.print_help()
            sys.exit(1)

    return parser.parse_args()


def _create(parser: argparse.ArgumentParser):
    """
    Handles adding the create arguments
    """

    ########################################################
    #  Below are the more common commands, with shortcuts  #
    ########################################################

    required = parser.add_argument_group("Required Arguments")
    optional = parser.add_argument_group("Optional Arguments")
    server = parser.add_argument_group(
        "Additional Server Flags (https://oitsjustjo.se/u/Z9mLwAY40)"
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

    optional.add_argument(
        "-b",
        "--backup",
        help="Enable backups every 30 minutes to the location provided. Example: -b './mc-backups'",
        default=None,
        required=False,
    )

    for env in SERVER_ENVS:
        server.add_argument(
            f"--{env}",
            required=False,
            type=SERVER_ENVS[env]["type"],
            help=SERVER_ENVS[env]["help"],
        )
