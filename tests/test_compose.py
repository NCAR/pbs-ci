from __future__ import absolute_import, division, print_function

import os
import subprocess

DOCKER_COMPOSE = os.path.join(os.path.dirname(__file__), "docker-compose.yml")


def test_docker_compose():
    cmd = ["pbs-ci-compose", "-f", DOCKER_COMPOSE]
    proc = subprocess.Popen(cmd)
    ret = proc.wait()
    assert ret == 0
