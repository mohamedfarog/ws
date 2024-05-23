from setuptools import find_packages
from setuptools import setup

setup(
    name='mina_ugv',
    version='0.0.0',
    packages=find_packages(
        include=('mina_ugv', 'mina_ugv.*')),
)
