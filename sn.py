#!/usr/bin/python3
import argparse
import os

versionString = 'SuperNamer 0.1'

class SuperNamer:
	'Class for dealing with renaming of files'
	#Init and parse input
	def __init__(self):
		self.argparse()
	#Parse input
	def argparse(self):
		parser = argparse.ArgumentParser(description='Rename files according to ruleset')
		#Custom code not ready yet
		#parser.add_argument('--custom', '-c', metavar='PYTHONCODE', help='Custom Python code subset for renaming files. WIP')
		parser.add_argument('--discard', '-d', type=int, metavar='INTEGER', help='Discards X characters from either the beginning or end of the filename. Negative numbers indicate discarding X characters from the end of the filename. First character is index 0. (Equivalent of "[:INTEGER]" in python)')
		parser.add_argument('--keep', '-k', type=int, metavar='INTEGER', help='Keeps X characters from either the beginning or end of the filename. Negative numbers indicate keeping X characters starting at the end of the filename. First character is index 0. (Equivalent of "[INTEGER:]" in python)')
		parser.add_argument('--replace', '-r', type=str, metavar='STRING,STRING', help='Replaces instances of first string with second string in a filename')
		parser.add_argument('--slice', '-s', type=str, metavar='START,STOP', help='Slices between two integers, representing start and stop values for a python slice. First character is index 0.')
		parser.add_argument('--version', '-v', action='version', version=versionString)
		parser.add_argument('--dryrun', '-D', action='store_true', default=False, help="Outputs filename changes, but doesn't touch the filesystem")
		parser.add_argument('--nonverbose', '-N', action='store_true', default=False, help="Don't display verbose output")
		parser.add_argument('files', nargs='+', help='Files to rename. Can be a single file, list of files (with spaces between), or a directory/directories (including .), but not mixed')

		#Get arguments
		self.args = parser.parse_args()
		self.rename()
	#Decide which method to use
	def rename(self):
		filesAreDirs = self.checkIfDirs()
		if filesAreDirs == True:
			files = []
			for dir in self.args.files:
				files.extend(os.listdir(dir))
			self.args.files = files
		elif filesAreDirs == "ERROR":
			print("ERROR: Mixed files and directories!")
			return

		if len(self.args.files) == 2 and self.args.discard == None and self.args.keep == None and self.args.replace == None and self.args.slice == None:
			self.singleRename(self.args.files[0], self.args.files[1])
		else:
			self.ruleRename()
	# Rename single file
	def singleRename(self, old, new):
		if not self.args.nonverbose:
			print(old+" changed to "+new)
		if self.args.dryrun == True:
			return
		os.rename(old, new)
	# Rename multiple files using ruleset
	def ruleRename(self):
		for file in self.args.files:
			newfile = self.applyRule(file)
			self.singleRename(file, newfile)
		#rename()
	#Apply rules to a filename
	def applyRule(self, file):
		if self.args.discard:
			file = file[:self.args.discard]
		if self.args.keep:
			file = file[self.args.keep:]
		if self.args.replace:
			#TODO: Make it possible to replace arbitrary numbers using ## syntax
			replace = self.args.replace.split(",")
			file = file.replace(replace[0], replace[1])
		if self.args.slice:
			slice = self.args.slice.split(",")
			file = file[int(slice[0]):int(slice[1])]
		return file
	#Check if given path is a directory
	def checkIfDirs(self):
		check = ""
		for path in self.args.files:
			if os.path.isdir(path):
				if(check != False):
					check = True
				else:
					return "ERROR"
			else:
				if(check != True):
					check = False
				else:
					return "ERROR"
		return check

SuperNamer()