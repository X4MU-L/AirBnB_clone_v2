#!/usr/bin/python3
"""use fabric to archive web_static files in the current folder"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """archives all web_static folder in the current direcory"""

    creat_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_%s.tgz" % (creat_time.strip())
    if not os.path.isdir("versions"):
        if local("mkdir versions").failed is True:
            return None

    if local("tar -cvzf %s web_static/" % (path)).failed is True:
        return None

    return path
