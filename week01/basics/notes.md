## Based on my personal understanding of the problem I did, the things that I undestand I right them in my own words. 
# Git Workflows

## Option 1 — Local → GitHub *(Beginner)*
1. Create folder → `git init` → commit → push to GitHub

g## Option 2 — GitHub → Local *(Team)*
1. Create repo on GitHub → `git clone <url>` → code → push

## Rule
- Solo → `git init` first
- Team → clone first

This notes.md is created for future reference for me & aswell as for anyone going through my repo.

Virutal environments(venv) is created to isolate libraries so they donot conflict each other or the system.

To create venv in py we use "python -m venv venv" and for activation of the "venv" venv/scripts/activate can be used.

pip is a tool that helps you download and manage py library

After this happens, pip install is used to download py libraries

you can download libraries using terminal (eg: pip install numpy) or download from requriements.txt (pip install -r requirements.txt)

while downloading a particular library other dependencies that the library relies on also gets added (eg: while pip install matplotlib is done)  
