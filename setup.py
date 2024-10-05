from setuptools import find_packages, setup

setup(
    name="romatch",
    packages=find_packages(include=("romatch*",)),
    version="0.0.1",
    author="Johan Edstedt",
    install_requires=open("requirements.txt", "r").read().split("\n"),
)
