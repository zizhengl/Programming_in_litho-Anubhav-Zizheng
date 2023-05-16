from setuptools import setup
from setuptools import find_packages

with open("README.txt","r") as fh:
    long_description = fh.read()

setup(
    name = "deUn",
    version = "0.0.1",
    author = "QPSI on Mar, 22nd, 2023",
    description = "A package that contains all the devices in QPSI.",
    packages=find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3.8",
        "Operating system:: Win"
    ],
    install_requires = [
        "gdshelpers",
        "gdspy",
        "gdsfactory",
        "geos",
        "numpy"
    ],
)