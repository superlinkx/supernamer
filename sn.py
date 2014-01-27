#!/usr/bin/python3
import argparse
from os import rename, listdir

versionString = 'SuperNamer 0.1'

class SuperNamer:
	'Class for dealing with renaming of files'
	#Init and parse input
	def __init__(self):
		#Parse Input
		parser = argparse.ArgumentParser(description='Rename files according to ruleset')
		parser.add_argument('--custom', '-c', metavar='PYTHONCODE', help='Custom Python code subset for renaming files. WIP')
		parser.add_argument('--discard', '-d', type=int, metavar='INTEGER', help='Discards X characters from either the beginning or end of the filename. Negative numbers indicate discarding X characters from the end of the filename. (Equivalent of "[:INTEGER]" in python)')
		parser.add_argument('--keep', '-k', type=int, metavar='INTEGER', help='Keeps X characters from either the beginning or end of the filename. Negative numbers indicate keeping X characters starting at the end of the filename. (Equivalent of "[INTEGER:]" in python)')
		parser.add_argument('--replace', '-r', type=str, metavar='STRING,STRING', help='Replaces instances of first string with second string in a filename')
		parser.add_argument('--slice', '-s', type=str, metavar='START,STOP', help='Slices between two integers, representing start and stop values for a python slice.')
		parser.add_argument('--rulestring', '-R', type=str, help='Use multiple rules at once. A rulestring is an array of rules, with each rule being an array containing the rule. e.g. --rulestring="[[-12],["hello","world"],[1,2]]" will keep last 12 characters, then rename instances of hello with world, and finally grab the character between positions 1 and 2.')
		parser.add_argument('--version', action='version', version=versionString)
		parser.add_argument('files', nargs='+', help='Files to rename. Can be a single file, list of files (with spaces between), or a directory (including .)')

		#Get arguments
		args = parser.parse_args()
		self.rename(args)
	#Decide which method to use
	def rename(self, args):
		if(len(args.files) == 2 and args.custom == None and args.discard == None and args.keep == None and args.replace == None and args.slice == None and args.rulestring == None):
			self.singleRename(args.files[0], args.files[1])
		else:
			self.ruleRename(args)		
	# Rename single file
	def singleRename(self, old, new):
		print("Old file: "+old+"; New file: "+new)
		#rename(old, new)
	# Rename multiple files using ruleset
	def ruleRename(self, args):
		print("Args: "+str(args))
		#rename()		

SuperNamer()