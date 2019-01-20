from __future__ import absolute_import, division, print_function

import ast
import os
import subprocess

import click
import docker

from . import __version__
from .utils import execute_cmd


class PythonLiteralOption(click.Option):
    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except Exception:
            raise click.BadParameter(value)


@click.command()
@click.version_option(version=__version__)
@click.option(
    "--cmd", cls=PythonLiteralOption, default=[], help=("Command to be executed")
)
@click.option(
    "--capture", type=bool, default=True, help=("Yield output line by line if True")
)
def main(cmd, capture):
    for line in execute_cmd(cmd, capture):
        print(line)


if __name__ == "__main__":
    main()
