from __future__ import absolute_import, division, print_function

import os
import subprocess
import time

import pytest

from pbs_ci.execute import execute_cmd

DOCKER_COMPOSE_FILE = os.path.join(os.path.dirname(__file__), "docker-compose.yml")


def docker_compose():
    cmd = ["docker-compose", "-f", DOCKER_COMPOSE_FILE, "up", "-d"]
    for line in execute_cmd(cmd, capture=False):
        pass


docker_compose()


def test_capture_cmd_no_capture_success():
    # This should succeed
    for line in execute_cmd(["/bin/bash", "-c", "echo test"]):
        pass


def test_capture_cmd_no_capture_fail():
    with pytest.raises(subprocess.CalledProcessError):
        for line in execute_cmd(["/bin/bash", "-c", "e "]):
            pass


def test_capture_cmd_capture_success():
    # This should succeed
    for line in execute_cmd(["/bin/bash", "-c", "echo test"], capture=True):
        assert line == "test\n"


def test_capture_cmd_capture_fail():
    with pytest.raises(subprocess.CalledProcessError):
        for line in execute_cmd(
            ["/bin/bash", "-c", "echo test; exit 1 "], capture=True
        ):
            assert line == "test\n"
