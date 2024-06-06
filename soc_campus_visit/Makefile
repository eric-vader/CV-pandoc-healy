TUT:=$(shell basename $(CURDIR))

default: 
	pandoc --include-in-header include-in-header.tex --filter mermaid-filter --highlight-style pygments -t beamer -V theme:metropolis -V aspectratio:169 $(TUT).md -o $(TUT).pdf