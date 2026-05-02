# Dev Notes
Based on my personal understanding of the problem I did, the things that I understand I right them in my own words.

---

## Git Workflows

### Option 1 — Local → GitHub *(Beginner)*
1. Create folder → `git init` → commit → push to GitHub

### Option 2 — GitHub → Local *(Team)*
1. Create repo on GitHub → `git clone <url>` → code → push

### Rule
- Solo → `git init` first
- Team → clone first

This notes.md is created for future reference for me & aswell as for anyone going through my repo.

---

## Virtual Environments (venv)

Virutal environments(venv) is created to isolate libraries so they donot conflict each other or the system.

To create venv in py we use `python -m venv venv` and for activation of the "venv" `venv/scripts/activate` can be used.

---

## pip

pip is a tool that helps you download and manage py library

After this happens, pip install is used to download py libraries

you can download libraries using terminal (eg: `pip install numpy`) or download from requriements.txt (`pip install -r requirements.txt`)

while downloading a particular library other dependencies that the library relies on also gets added (eg: while pip install matplotlib is done)

---

## Day 2

; is used to seperate the code the next line in language in py it is done already but incase you need to have two block of code in same link then ; is still needed

data type of variables are defined before manual creation we donot need to do declare it

---

## Day 3

Boolean is another data type which logically gives output in True/False.

Boolean interpets every non zero value as True (eg: 1, 34.32, hello) and every zero/none value as False (eg : 0, 0.0, {}, (), none). 

We use f string if we want to display a varaible as an string inside print, it allows variable to act as a string.