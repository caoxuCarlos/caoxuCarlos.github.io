#! /bin/bash

python3 chart_generator.py

git add -A

git commit -m"Update body data."

git push
