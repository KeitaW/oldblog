#!/bin/bash
make html
ghp-import output
git push https://github.com/keitaw/keitaw.github.io.git gh-pages:master
