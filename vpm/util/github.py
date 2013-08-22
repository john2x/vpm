import json
import urllib

from config import *

def _search_cache(plugin_name):
    plugin_name = args.plugin_name
    with open(VPM_REPO_FILE, 'r') as repo_file:
        repos = json.load(repo_file)
    results = []
    plugin_name == plugin_name.lower()
    for k, v in repos.items():
        if plugin_name in k.lower():
            desc, url = v
            results.append((k, desc, url))
    return results

def search_vim_scripts(plugin_name):
    repo = urllib.urlopen(VIM_SCRIPTS_REPO + plugin_name)
    repo = json.load(repo)
    if repo.get('message') == 'Not Found':
        return None
    return repo['name'], repo['description'], repo['clone_url']

def to_clone_url(project_url):
    base = 'https://github.com/%s/%s.git'
    username, _, project = project_url.partition('/')
    return base % (username, project)
