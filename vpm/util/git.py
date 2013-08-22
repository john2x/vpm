# Git helpers

import os
import subprocess
import ConfigParser
from config import *
from errors import *

def which_git():
    try:
        git = subprocess.check_output(['which', 'git'])
    except subprocess.CalledProcessError:
        raise CommandNotFound('git')
    return git.strip()

def git_command():
    cp = ConfigParser.ConfigParser()
    with open(VPM_CONFIG_FILE, 'rb') as config:
        cp.readfp(config)
    if cp.has_section('Git'):
        return cp.get('Git', 'git')
    return which_git()

def clone(clone_url, plugin_name):
    git = git_command()
    if not git:
        raise CommandNotFound('git')
    clone_path = os.path.join(VPM_BUILD_DIR, plugin_name)
    command = (
        git, 'clone',
        clone_url, clone_path,
    )
    print 'Cloning %s...' % clone_url
    try:
        pr = subprocess.check_call(command)
    except subprocess.CalledProcessError, e:
        raise CommandFailed(e)
    return clone_path

