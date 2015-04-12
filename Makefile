all: set-executables clean-files

set-executables:
	@find bin -not -name _* | xargs chmod +x # Exclude files beginning with a dash for executables

clean-files: clean-pyc-files

clean-pyc-files:
	@find . -name *.pyc | xargs rm -f