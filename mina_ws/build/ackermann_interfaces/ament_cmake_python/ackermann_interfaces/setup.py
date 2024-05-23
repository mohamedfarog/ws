from setuptools import find_packages
from setuptools import setup

setup(
    name='ackermann_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('ackermann_interfaces', 'ackermann_interfaces.*')),
)
