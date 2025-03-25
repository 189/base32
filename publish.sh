#!/usr/bin/env bash

dest=$1

rm -rf ./build
rm -rf ./dist

python -m build

if [[ ${dest} = "main"  ]]; then
    echo "pending to publish main pypi"
    twine upload  dist/*
else
    echo "pending publish to test.pypi.org"
    twine upload --verbose --repository-url https://test.pypi.org/legacy/  dist/*
fi
echo "finished publish"
    



