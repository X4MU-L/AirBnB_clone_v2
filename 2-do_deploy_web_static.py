#!/usr/bin/python3
"""use fabric to archive web_static files in the current folder"""

import os
from fabric.api import put, run, env

env.hosts = ['18.210.33.133', '35.174.200.184']


def do_deploy(archive_path):
    """Deploys an archive to the web servers."""
    if os.path.isfile(archive_path) is False:
        return False

    _file = archive_path.split('/')[-1].split('.')[0]
    r_path = "/data/web_static/releases"

    if put(archive_path, '/tmp/{}.tgz'.format(_file)).failed is True:
        return False

    if run('rm -rf {}/{}'.format(r_path, _file)).failed is True:
        return False

    if run('mkdir -p {}/{}/'.format(r_path, _file)).failed is True:
        return False

    if run('tar -xzf /tmp/{}.tgz -C {}/{}/'
           .format(_file, r_path, _file)).failed is True:
        return False

    if run('rm /tmp/{}.tgz'.format(_file)).failed is True:
        return False

    command = "mv {}/{}/web_static/*".format(r_path, _file)
    command += " {}/{}/".format(r_path, _file)
    if run(command).failed is True:
        return False

    if run('rm -rf {}/{}/web_static'
           .format(r_path, _file)).failed is True:
        return False
