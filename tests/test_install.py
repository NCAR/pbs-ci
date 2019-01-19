from __future__ import absolute_import, division, print_function

import os
import subprocess

import docker

DOCKER_COMPOSE = os.path.join(os.path.dirname(__file__), "docker-compose.yml")

client = docker.from_env()


def test_install():
    compose_cmd = ["pbs-ci-compose", "-f", DOCKER_COMPOSE]
    install_cmd = ["pbs-ci-install", "pbs_master", "echo Hello World!"]
    proc_1 = subprocess.Popen(compose_cmd)
    ret_1 = proc_1.wait()
    proc_2 = subprocess.Popen(install_cmd)
    ret_2 = proc_2.wait()
    assert ret_1 == 0
    assert ret_2 == 0
