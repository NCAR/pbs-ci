from __future__ import absolute_import, division, print_function

import ast
import os

import click
import docker

from . import __version__


class PythonLiteralOption(click.Option):
    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except Exception:
            raise click.BadParameter(value)


@click.command()
@click.version_option(version=__version__)
@click.option("--user", type=str, default="", help=("User to execute command as"))
@click.option("--container", type=str, help=("Container"))
@click.option(
    "--cmd", cls=PythonLiteralOption, default=[], help=("Command to be executed")
)
def main(user, container, cmd):
    client = docker.from_env()
    containers = client.containers
    container = containers.get(container)
    ret = container.exec_run(cmd=cmd, user=user)
    if ret.exit_code != 0:
        raise ret
    return


if __name__ == "__main__":
    main()
