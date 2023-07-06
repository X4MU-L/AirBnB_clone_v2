#!/usr/bin/python3
"""This script generates a .tgz archive from the contents of a directory.
        * The name format of the file:
            web_static_<year<month><day><hour><minute><seconds>.tgz
"""
import os
from datetime import datetime
from fabric import api as fab


def do_pack():
    """Creates a .tgz archive file."""
    dt = datetime.strftime(datetime.utcnow(), '%Y%m%d%H%M%S')
    file_path = "versions/web_static_{}.tgz".format(dt)
    if not os.path.isdir('versions'):
        if fab.local('mkdir -p versions').return_code != 0:
            return None
    command = "tar -cvzf {} web_static".format(file_path)
    if fab.local(command).return_code != 0:
        return None
    return file_path
