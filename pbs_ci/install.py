from __future__ import absolute_import, division, print_function

import os

import click
import docker

from . import __version__


@click.command()
@click.version_option(version=__version__)
@click.argument("container", type=str)
@click.argument("cmd", type=(str, list))
def main(container, cmd):
    client = docker.from_env()
    containers = client.containers
    container = containers.get(container)
    ret = container.exec_run(cmd)
    if ret.exit_code != 0:
        raise ret
    return


if __name__ == "__main__":
    main()
