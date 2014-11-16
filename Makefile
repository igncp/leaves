all: install-tools set-executable-perms

install-tools: i-csv-tools i-jq make-vendors-executable

i-csv-tools:
	@sudo pip install csvkit

i-jq:
	@curl -s http://stedolan.github.io/jq/download/linux64/jq > vendors/jq
	@echo 'Downloaded jq for Linux 64. If that is not your case, download it, place it under vendors with jq name and make it executable'

set-executable-perms:
	@chmod +x ./bin/*
	@chmod +x ./vendors/*
	@chmod +x ./tools/*
