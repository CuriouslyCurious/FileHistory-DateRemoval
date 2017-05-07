#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Removes a specified string from all files in the FileHistory directory created by Windows 10 
(which for some reason actually RENAMES the files to old name + the current date...).
"""

import sys
import os

rm_string = r" (2017_05_05 09_29_25 UTC)" # <---- Replace this with whatever string you need to remove. NOTE the space.
found_file_history = False

for thing in os.listdir(os.getcwd()):
	if "FileHistory" == thing:
		walk_dir = os.getcwd()+thing
		found_file_history = True
		print("Found %s" % walk_dir)

if not found_file_history:		
	sys.exit()

count = 0
failed = 0
	
for root, subdirs, files in os.walk(walk_dir):
	for filename in files:
		file_path = os.path.join(root, filename)
		if filename.endswith(rm_string):
			if "~" in filename: # Tildes apparently break os.rename()
				try:  #Tries to replace tildes with spaces
					#print("\n%s \nto \n%s" % (file_path, file_path.replace("~", " ").replace(rm_string, "")))
					os.rename(file_path, file_path.replace("~", " ").replace(rm_string, ""))
					count += 1
				except OSError:
					print("Could not rename %s, skipping..." % file_path)
					failed += 1
				except FileExistsError:
					print("Could not rename %s, file already exists, skipping..." % file_path)
					failed += 1
			else:
				#print("\n%s \nto \n%s" % (file_path, file_path.replace(rm_string, "")))
				try:
					os.rename(file_path, file_path.replace(rm_string, ""))
					count += 1
				except FileExistsError:
					print("Could not rename %s, file already exists, skipping..." % file_path)
					failed += 1

print("====================")					
print("Finished.")
print("%d file(s) succesfully renamed." % count)
print("%d file(s) failed to be renamed." % failed)
print("====================")