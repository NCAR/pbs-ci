from __future__ import absolute_import, division, print_function

import os
import subprocess

import docker
import sleep

DOCKER_COMPOSE = os.path.join(os.path.dirname(__file__), "docker-compose.yml")

client = docker.from_env()


def test_script():
    compose_cmd = ["pbs-ci-compose", "-f", DOCKER_COMPOSE]
    script_cmd = [
        "pbs-ci-script",
        "--user",
        "pbsuser",
        "--container",
        "pbs_master",
        "--cmd",
        '["/bin/bash", "-c","python --version; echo Hello world; bash --version"]',
    ]
    proc_1 = subprocess.Popen(compose_cmd)
    ret_1 = proc_1.wait()
    sleep(20)
    proc_2 = subprocess.Popen(script_cmd)
    ret_2 = proc_2.wait()
    assert ret_1 == 0
    assert ret_2 == 0
