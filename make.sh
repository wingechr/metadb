#!/usr/bin/env bash

export PYTHONPATH=src

pipreqs --use-local --force --encoding utf8 --savepath requirements.txt .
sphinx-apidoc -H "Code" -o docs/_apidoc src

echo "BUILD docs (A): ./setup.py build_sphinx"
echo "BUILD docs (A): sphinx-build -a -n -b html -c . docs build/html"
echo "TEST (A): ./setup.py test"
echo "TEST (B): python -m unittest discover"
echo "BUILD sourcedist: ./setup.py sdist"
echo "BUILD: ./setup.py build"
