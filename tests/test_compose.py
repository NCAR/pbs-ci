from __future__ import absolute_import, division, print_function

import os
import subprocess

import docker

DOCKER_COMPOSE = os.path.join(os.path.dirname(__file__), "docker-compose.yml")

client = docker.from_env()


def test_docker_compose():
    cmd = ["pbs-ci-compose", "-f", DOCKER_COMPOSE]
    proc = subprocess.Popen(cmd)
    ret = proc.wait()
    assert ret == 0

    images = [client.images.get("andersy005/pbs")]
    assert len(images) == 1

    containers = [client.containers.get("pbs_master")]
    assert len(containers) == 1
