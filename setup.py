#!/usr/bin/env python

"""The setup script."""

from os.path import exists

from setuptools import find_packages, setup

import versioneer

readme = open("README.rst").read() if exists("README.rst") else ""
requirements = ["click", "docker"]


setup(
    name="pbs-ci",
    description="Continuous integration utility for PBS",
    long_description=readme,
    maintainer="Anderson Banihirwe",
    maintainer_email="abanihi@ucar.edu",
    url="https://github.com/NCAR/pbs-ci",
    packages=find_packages(),
    package_dir={"pbs-ci": "pbs-ci"},
    include_package_data=True,
    install_requires=requirements,
    license="Apache 2.0",
    zip_safe=False,
    keywords="pbs-ci",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    entry_points="""
          [console_scripts]
          pbs-ci-install=pbs_ci.install:main
          pbs-ci-compose=pbs_ci.compose:docker_compose
          pbs-ci-script=pbs_ci.script:main
          """,
)
