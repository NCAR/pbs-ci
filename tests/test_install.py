from __future__ import absolute_import, division, print_function

import os
import subprocess

import docker

DOCKER_COMPOSE = os.path.join(os.path.dirname(__file__), "docker-compose.yml")

client = docker.from_env()


def test_install():
    compose_cmd = ["pbs-ci-compose", "-f", DOCKER_COMPOSE]
    install_cmd = [
        "pbs-ci-install",
        "pbs_master",
        "/bin/bash",
        "-c",
        "echo Hello World!",
    ]
    subprocess.Popen(compose_cmd)
    ret = subprocess.Popen(install_cmd)
    assert ret == 0
