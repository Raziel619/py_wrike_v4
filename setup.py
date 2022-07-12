from pkg_resources import parse_requirements
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="py_wrike",
    version="0.1",
    license="MIT",
    author="Govinda Hosein",
    author_email="raziel619dev@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/Raziel619/py_wrike",
    keywords="wrike",
    install_requires=required,
)
