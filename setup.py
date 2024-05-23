#!/usr/bin/env python

from distutils.core import setup

setup(
    name='jellyfin-rpc',
    version='1.0',
    description='Jellyfin Music RPC for Discord',
    author='iiPython',
    author_email='ben@iipython.dev',
    url='https://github.com/iiarchives/jellyfin-rpc',
    scripts = [ 'scripts/mpris-rpc.py', 'scripts/jellyfin-rpc.py' ],
    install_requires = [
        'pydbus',
        'pypresence'
    ]
)
