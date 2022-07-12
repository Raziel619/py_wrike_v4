from setuptools import setup, find_packages

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
    install_requires=["certifi", "charset-normalizer", "idna", "requests", "urllib3"],
)
