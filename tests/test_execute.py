from __future__ import absolute_import, division, print_function

import os
import subprocess
import time

import docker
import pytest

DOCKER_COMPOSE = os.path.join(os.path.dirname(__file__), "docker-compose.yml")

client = docker.from_env()


@pytest.mark.parametrize(
    "cmd",
    [
        [
            "pbs-ci-execute",
            "--user",
            "pbsuser",
            "--container",
            "pbs_master",
            "--cmd",
            '["/bin/bash", "-c","python --version; echo Hello world; bash --version"]',
        ],
        [
            "pbs-ci-execute",
            "--container",
            "pbs_master",
            "--cmd",
            '["/bin/bash", "-c","python --version; echo Hello world; bash --version"]',
        ],
    ],
)
def test_exec(cmd):
    compose_cmd = ["pbs-ci-compose", "-f", DOCKER_COMPOSE]
    proc_1 = subprocess.Popen(compose_cmd)
    ret_1 = proc_1.wait()
    time.sleep(20)
    proc_2 = subprocess.Popen(cmd)
    ret_2 = proc_2.wait()
    assert ret_1 == 0
    assert ret_2 == 0
