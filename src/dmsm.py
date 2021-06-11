"""
Author: Jose Stovall | oitsjustjose
"""

import sys
from argparse import Namespace

from args import get_args
from docker_mgr import ServerManager


def main(args: Namespace) -> None:
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
        mgr.stop_server(force="-f" in sys.argv or "--force" in sys.argv)
    elif action == "restart":
        mgr.restart_server(force="-f" in sys.argv or "--force" in sys.argv)
    elif action == "delete":
        mgr.delete_server()
    elif action == "status":
        mgr.get_status()
    elif action == "console":
        mgr.open_console()
    elif action == "logs":
        mgr.logs()


if __name__ == "__main__":
    main(get_args())
