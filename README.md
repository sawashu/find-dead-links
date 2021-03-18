# find-dead-links

This application displays any dead links contained at the given URL. It keeps on searching dead links following with a given depth.

## Dependencies

`virtualenv` and `python3` are necessary to execute this application.

## Installation

Type `make install` installs `find-dead-links` into your `~/bin`
If you prefer to install it in another directory, type `make install INSTALL_DIR=<PREFERED_DIR>`

## Running

`find-dead-links <url>` - Finds all dead links in the given url

`find-dead-links -<depth> <url>` - Finds all dead links from not only the given url, but also any accessible links in that url recursively according to the given depth.
