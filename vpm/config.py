import os

DEBUG = True
DEFAULT_PATHOGEN_PATH = os.path.expanduser('~/.vim/bundle')
VPM_HOME = os.path.expanduser('~/.vpm')
VPM_BUILD_DIR = os.path.join(VPM_HOME, 'build')
VPM_CONFIG_FILE = os.path.join(VPM_HOME, 'vpmrc')
VPM_REPO_FILE = os.path.join(VPM_HOME, '.repos')
VPM_INSTALLED_PLUGINS_FILE = os.path.join(VPM_HOME, '.installed_plugins')
VIM_SCRIPTS_REPOS = 'https://api.github.com/users/vim-scripts/repos'
VIM_SCRIPTS_REPO = 'https://api.github.com/repos/vim-scripts/'

