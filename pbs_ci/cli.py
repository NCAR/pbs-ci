from __future__ import absolute_import, division, print_function

import os

import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    print("Hello World")


if __name__ == "__main__":
    main()
