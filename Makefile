
INSTALL_DIR = $(dirname ${BASH_SOURCE[0]})



install:
	cp find-dead-links ${INSTALL_DIR}
	virtualenv -p python3 find_dead_links_env
	source ${INSTALL_DIR}/find_dead_links_env/bin/activate
	pip3 install beautifulsoup
	pip3 install requests
	pip3 install sys	
