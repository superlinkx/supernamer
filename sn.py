#!/usr/bin/python3
from os import rename, listdir

# Rename single file
def singleRename(old, new):
	rename(old, new)

file = input("Enter a file")
name = input("Enter a new name")
singleRename(file, name)	