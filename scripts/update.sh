#!/bin/bash

# Remove old distribution files
rm -rf dist/*

# Create new distribution package
python3 setup.py sdist bdist_wheel

# Upload the new distribution to PyPI
python3 -m twine upload dist/*

# Print done
echo "Package updated and uploaded to PyPI successfully!"