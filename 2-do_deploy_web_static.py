#!/usr/bin/python3
"""
    This scripts updates the web servers with an archive.
"""
import os.path
from fabric.api import env, put, run


env.hosts = ['52.87.215.172', '100.26.231.127']


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
           .format(r_path, _file, _file)).failed is True:
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

    if run('rm -rf /data/web_static/current').failed is True:
        return False

    if run('ln -s {}/{} /data/web_static/current'
           .format(r_path, _file)).failed is True:
        return False
    return True
