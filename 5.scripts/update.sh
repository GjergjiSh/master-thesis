#!/bin/bash

git add .
git commit -m "updates"

if [ "$1" = "-p" ]; then
    git push
fi