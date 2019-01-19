from __future__ import absolute_import, division, print_function

import os

import click

DOCKER_COMPOSE = os.path.join(os.path.dirname(__file__), "docker-compose.yml")


@click.command()
def main():
    print("Hello World")


if __name__ == "__main__":
    main()
