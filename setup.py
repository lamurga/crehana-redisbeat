try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

install_requires = [
    "celery == 4.1.0",
    "redis == 2.10.6",
    "tenacity >= 5.0.3",
    "mock >= 2.0.0"
]

setup(
    name="redisbeat",
    version="1.0.0",
    author="lamurga",
    download_url="https://github.com/lamurga/crehana-redisbeat",
    description="Python library for crehana",
    install_requires=install_requires
)
