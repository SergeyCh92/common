from setuptools import setup, find_namespace_packages
from pathlib import Path

with open(Path(__file__).parent.joinpath("requirements.txt")) as file:
    requirements = [line.strip() for line in file]

setup(
    name="common_core",
    version="1.0.0",
    author="Chaban Sergey",
    packages=find_namespace_packages(include=["common.*"]),
    install_requires=requirements,
)
