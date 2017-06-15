import os

from setuptools import setup, find_packages


def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'goonj/version.py')) as f:
        locals = {}
        exec (f.read(), locals)
        return locals['VERSION']
    raise RuntimeError('No version info found.')


setup(
    name='goonj',
    version=get_version(),
    packages=find_packages(exclude=['tests', 'samples']),
    install_requires=[
        'click>=3.0.0',
    ],
    url='',
    license='BSD',
    author='bkp',
    author_email='bibek.padhy@treebohotels.com',
    entry_points={
        'console_scripts': [
            'goonj = goonj.cli:main',

        ],
    },
    test_suite="tests",
    description='A python library to enable easy alerting services across multiple channels.'
)
