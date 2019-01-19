from __future__ import absolute_import, division, print_function

import os
import subprocess

import click

DOCKER_COMPOSE = os.path.join(os.path.dirname(__file__), "docker-compose.yml")


@click.command()
def docker_compose():
    print("Building and running PBS with Compose")
    cmd = ["docker-compose", "-f", DOCKER_COMPOSE, "up", "-d"]
    proc = subprocess.Popen(cmd)
    ret = proc.wait()

    if ret != 0:
        raise subprocess.CalledProcessError(ret, cmd)
    return


if __name__ == "__main__":
    docker_compose()
