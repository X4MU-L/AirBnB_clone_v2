#!/usr/bin/python3
"""use fabric to archive web_static files in the current folder"""

import os
from fabric.api import put, run, env

env.hosts = ['18.210.33.133', '35.174.200.184']


def do_deploy(archive_path):
    """Deploys an archive to the web servers."""
    if os.path.isfile(archive_path) is False:
        return False

    file_name = archive_path.split("/")[-1].split(".")[0]
    save_path = "/data/web_static/releases/"

    if put(archive_path, "/tmp/{}.tgz".format(file_name)).failed is True:
        return False

    if run('rm -rf {}/{}'.format(save_path, file_name)).failed is True:
        return False

    if run("mkdir -p {}{}/".format(save_path, file_name)).failed is True:
        return False

    if run("tar -xvf /tmp/{}.tgz -C {}{}/".format(
        file_name, save_path, file_name
    )).failed is True:
        return False

    if run("rm /tmp/{}.tgz".format(file_name)).failed is True:
        return False

    mv_files = "mv {}{}/web_static/*".format(save_path, file_name)
    mv_files += " {}{}/".format(save_path, file_name)
    if run(mv_files).failed is True:
        return False

    if run('rm -rf {}{}/web_static'
           .format(save_path, file_name)).failed is True:
        return False

    if run('rm -rf /data/web_static/current').failed is True:
        return False

    if run('ln -s {}{} /data/web_static/current'
           .format(save_path, file_name)).failed is True:
        return False
    return True
