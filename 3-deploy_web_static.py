#!/usr/bin/python3
"""use fabric to archive web_static files in the current folder"""

import os
from fabric.api import env, execute

env.hosts = ['18.210.33.133', '35.174.200.184']

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """"Execute do_pack and do_deploy"""
    file = execute(do_pack)
    if file:
        return do_deploy(list(file.values()[0]))
