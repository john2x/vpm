import json
import os
import shutil
import ConfigParser
from config import *
from errors import *

def bundle_path():
    cp = ConfigParser.ConfigParser()
    with open(VPM_CONFIG_FILE, 'rb') as config:
        cp.readfp(config)
    if not cp.has_section('Pathogen'):
        raise SetupError("pathogen_path not found. Run 'vpm configure' first.")
    pathogen_path = cp.get('Pathogen', 'pathogen_path')
    if not pathogen_path:
        raise SetupError("pathogen_path not found. Run 'vpm configure' first.")
    return pathogen_path

def cleanup_build_dir():
    print 'Cleaning up...'
    shutil.rmtree(VPM_BUILD_DIR)
    os.mkdir(VPM_BUILD_DIR)

def get_installed(plugin_name):
    plugins = {}
    with open(VPM_INSTALLED_PLUGINS_FILE, 'rb') as installed:
        try:
            plugins = json.load(installed)
        except ValueError:
            pass
    plugin_name = plugin_name.lower()
    for k, v in plugins.items():
        if plugin_name == k.lower():
            # verify plugin is still in install path
            if not os.path.exists(v[1]):
                return None
            return k, v[0], v[1]
    return None

def is_installed(plugin_name):
    plugin = get_installed(plugin_name)
    return bool(plugin)

def update_installed_list(plugin_name, clone_url, clone_path):
    plugins = {}
    with open(VPM_INSTALLED_PLUGINS_FILE, 'rb') as installed:
        try:
            plugins = json.load(installed)
        except ValueError:
            pass
    plugins[plugin_name] = (clone_url, clone_path)
    with open(VPM_INSTALLED_PLUGINS_FILE, 'wb') as installed:
        json.dump(plugins, installed)

def cleanup_installed_list(plugin_name):
    plugins = {}
    with open(VPM_INSTALLED_PLUGINS_FILE, 'rb') as installed:
        try:
            plugins = json.load(installed)
        except ValueError:
            pass
    if plugin_name in plugins.keys():
        plugins.pop(plugin_name)
    with open(VPM_INSTALLED_PLUGINS_FILE, 'wb') as installed:
        json.dump(plugins, installed)

