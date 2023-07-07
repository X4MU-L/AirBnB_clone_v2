#!/usr/bin/python3
"""
    This scripts updates the web servers with an archive.
"""
import os.path
from fabric.api import hosts, put, run


@hosts(['52.87.215.172', '100.26.231.127'])
def do_deploy(archive_path):
    """Deploys an archive to the web servers."""
    if os.path.isfile(archive_path) is False:
        return False

    _file = archive_path.split('/')[-1].split('.')[0]

    if put(archive_path, '/tmp/{}.tgz'.format(_file)).failed is True:
        return False

    if run('mkdir -p /data/web_static/releases/{}/'
           .format(_file)).failed is True:
        return False

    if run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
           .format(_file, _file)).failed is True:
        return False

    if run('rm /tmp/{}.tgz'.format(_file)).failed is True:
        return False

    command = "mv /data/web_static/releases/{}/web_static/*"\
        .format(_file)
    command += " /data/web_static/releases/{}/".format(_file)
    if run(command).failed is True:
        return False

    if run('rm -rf /data/web_static/releases{}/web_static'
           .format(_file)).failed is True:
        return False

    if run('rm -rf /data/web_static/current').failed is True:
        return False

    if run('ln -s /data/web_static/releases/{} /data/web_static/current'
           .format(_file)).failed is True:
        return False
    return True
