# Author: Daniel Nicolas Gisolfi

source := $(shell ls | grep *.md)
title=$(shell grep -m 1 title $(source) | cut -d ':' -f2 | xargs)
version=$(shell grep -m 1 version $(source) | cut -d ':' -f2 | xargs)
flags=--allow-local-files --theme dracula.css
devflags=--server --watch --allow-local-files

.PHONY: pptx
pptx:
	marp $(flags) $(source) -o $(title)-$(version).pptx

.PHONY: pdf
pdf:
	marp $(flags) $(source) -o $(title)-$(version).pdf

.PHONY: html
html:
	marp $(flags) $(source) -o $(title)-$(version).html

.PHONY: dev
dev:
	marp $(devflags) .

