# Copyright (c) 2017, Project Jupyter Contributors
# All rights reserved.
# Borrows heavily from repo2docker project

import subprocess
from functools import partial


def execute_cmd(cmd, capture=True, **kwargs):
    """
    Call given command, yielding output line by line if capture=True.
    Must be yielded from.
    """
    if capture:
        kwargs["stdout"] = subprocess.PIPE
        kwargs["stderr"] = subprocess.STDOUT

    proc = subprocess.Popen(cmd, **kwargs)

    if not capture:
        # not capturing output, let subprocesses talk directly to terminal
        ret = proc.wait()
        if ret != 0:
            raise subprocess.CalledProcessError(ret, cmd)
        return

    # Capture output for logging.
    # Each line will be yielded as text.
    # This should behave the same as .readline(), but splits on `\r` OR `\n`,
    # not just `\n`.
    buf = []

    def flush():
        """Flush next line of the buffer"""
        line = b"".join(buf).decode("utf8", "replace")
        buf[:] = []
        return line

    c_last = ""
    try:
        for c in iter(partial(proc.stdout.read, 1), b""):
            if c_last == b"\r" and buf and c != b"\n":
                yield flush()
            buf.append(c)
            if c == b"\n":
                yield flush()
            c_last = c
    finally:
        ret = proc.wait()
        if ret != 0:
            raise subprocess.CalledProcessError(ret, cmd)
