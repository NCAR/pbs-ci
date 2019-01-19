from __future__ import absolute_import, division, print_function

import os
import subprocess

import click


@click.command()
@click.option(
    "-f",
    "--compose_file",
    type=click.Path(exists=True),
    show_default=True,
    help=("Specify a compose file"),
)
def docker_compose(compose_file):
    print("Building and running PBS with Compose")
    cmd = ["docker-compose", "-f", compose_file, "up", "-d"]
    proc = subprocess.Popen(cmd)
    ret = proc.wait()

    if ret != 0:
        raise subprocess.CalledProcessError(ret, cmd)
    return


if __name__ == "__main__":
    docker_compose()
