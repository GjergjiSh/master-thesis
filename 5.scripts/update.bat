@echo off
git add .
git commit -m "updates"

if "%1"=="-p" (
    git push
)