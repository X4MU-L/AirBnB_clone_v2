#!/usr/bin/python3
"""use fabric to archive web_static files in the current folder"""

from fabric.api import env, run

env.hosts = ['18.210.33.133', '35.174.200.184']


def do_clean(number=0):
    number = 1 if number <= 0 else number
    cleans = ["versions/", "/data/web_static/releases/"]
    for dirs_ in cleans:
        files = run("ls -cltr {dirs_} | awk '{print $NF}'",
                    hide=True).stdout.split()
        count = 0
        for file in files:
            if run(f"test -f {file} && echo 'True' || echo 'False'", hide=True).stdout.strip() == 'True':
                if count >= number:
                    run(f"rm {file}")
                    print(f"Deleted file: {file}")
                else:
                    count += 1
