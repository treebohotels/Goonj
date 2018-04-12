import os

from setuptools import setup, find_packages


def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, 'goonj/version.py')) as f:
        locals = {}
        exec(f.read(), locals)
        return locals['VERSION']
    raise RuntimeError('No version info found.')


setup(
    name='goonj',
    version=get_version(),
    packages=find_packages(exclude=['tests', 'samples']),
    install_requires=[
        'yml==0.0.1',
        'request==0.0.26',
        'PyYAML==3.12',
        'requests==2.18.4',
        'pre-commit==1.7.0',
        'pre-commit-hooks==1.2.3 '

    ],
    url='',
    license='BSD',
    author='sohit kumar,bkp',
    author_email='sohit.kumar@treebohotels.com,bibek.padhy@treebohotels.com',
    test_suite="tests",
    description='A python library to enable easy alerting services across multiple channels.')
