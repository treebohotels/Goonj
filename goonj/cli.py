# -*- coding: utf-8 -*-
"""
cli for goonj
"""

import logging

import click
import constants
import os

logging.basicConfig()


@click.group()
def main():
    """goonj command line tool"""
    pass


@main.command()
@click.argument("type")
@click.option("-u", "--url",
              help="test help",
              default="test")
def start(type, url):
    """command to start the service"""
    logger = logging.getLogger("goonj:start")


@main.command()
@click.argument('type')
def stop(type):
    """command to stop the processes"""
    logger = logging.getLogger("goonj:stop")


@main.command()
def info():
    """show the state of the service"""
    logger = logging.getLogger("goonj:info")
