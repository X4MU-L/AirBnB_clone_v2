#!/usr/bin/python3
"""use fabric to archive web_static files in the current folder"""

from fabric.api import env, run, local

env.hosts = ['18.210.33.133', '35.174.200.184']


def do_clean(number=0):
    """"cleans up old versions of archives"""
    number = int(number)
    number = 1 if number <= 0 else number
    _to_clean = ["versions/", "/data/web_static/releases/"]
    for dirs_ in _to_clean:
        files = ""
        if dirs_ == "versions/":
            files = local("ls -clt %s | awk '{print $NF}'" % (dirs_),
                          capture=True).stdout.split()
            for file_ in files[1 + number:]:
                local("rm %s%s" % (dirs_, file_))
                print("Deleted file: %s" % (file_))
        else:
            files = run(
                "ls -clt %s | awk '{print $NF}'" % (dirs_)).stdout.split()
            files.remove("test")
            for file_ in files[1 + number:]:
                run("rm -rf %s%s" % (dirs_, file_))
                print("Deleted directory: %s" % (file_))
