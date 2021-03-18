
SHELL =/bin/bash
INSTALL_DIR = ~/bin
SCRIPT_DIR = ${INSTALL_DIR}/find-dead-links
PYFILE_DIR = ${INSTALL_DIR}/find-dead-links.py
ENV_INSTALL = ${INSTALL_DIR}/fdl-env/bin/activate

install: ${SCRIPT_DIR} ${PYFILE_DIR} ${ENV_INSTALL}

${SCRIPT_DIR}: find-dead-links
	cp -f $^ ${INSTALL_DIR}
	chmod 700 $@

${PYFILE_DIR}: find-dead-links.py
	cp -f $^ ${INSTALL_DIR}
	chmod 700 $@

${ENV_INSTALL}:
	virtualenv -p python3 ${INSTALL_DIR}/fdl-env
	chmod 700 $@
	source $@ && pip3 install beautifulsoup4 && pip3 install requests


