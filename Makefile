all: install-tools set-executable-perms 

install-tools: i-python-modules i-jq

i-python-modules:
	@sudo pip install csvkit
	@sudo pip install nose
	@sudo pip install pygithub
	@sudo pip install requests
	@sudo pip install requests_oauthlib
	@sudo pip install python-linkedin
	@sudo pip install pymongo
	sudo apt-get install python-matplotlib python-tk python-pandas

i-jq:
	@curl -s http://stedolan.github.io/jq/download/linux64/jq > vendors/jq
	@echo 'Downloaded jq for Linux 64. If that is not your case, download it, place it under vendors with jq name and make it executable'

set-executable-perms:
	@chmod +x ./bin/*
	@chmod +x ./vendors/*
	@chmod +x ./tools/*
