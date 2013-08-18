Vim Plugin/Pathogen Manager
===========================

The missing plugin manager for Vim.

Prerequisites
-------------

**vpm** works on top of Pathogen to manage Vim plugins.
[Install Pathogen][pathogen] first.

Install
-------

Make sure [Pathogen][pathogen] is installed and properly setup.

Copy `vpm` into your `$PATH` (e.g. `/usr/local/bin`) and make it executable.

    $ chmod +x vpm

Then run `$ vpm configure` to get started.

Usage
-----

    $ vpm configure
    $ vpm install <plugin-name>
    $ vpm update <plugin-name>
    $ vpm uninstall <plugin-name>
	$ vpm list-installed

For a list of all available scripts, see [vim-scripts.org](http://vim-scripts.org/vim/scripts.html)

Limitations
-----------

1. For now, the plugin needs to be on the [vim-scripts][vim-scripts] project on
   Github.
2. The plugin needs to [Pathogen][pathogen] compatible.

TODO/Goals
----------

1. Support for plugins outside of [vim-scripts][vim-scripts]
2. Support for plugins not compatible with Pathogen by default
3. Support for plugins outside of Github?
4. Run `:helptags` after install
5. Windows support?
6. Be the de-facto standard for Vim plugin management and rule the world. Muahahaha!

License
-------

Same as [Vim's][vim]. See `:help license`.

[pathogen]: https://github.com/tpope/vim-pathogen
[vim-scripts]: https://github.com/vim-scripts?tab=repositories
[vim]: http://www.vim.org/about.php

