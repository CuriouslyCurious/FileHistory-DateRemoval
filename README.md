# FileHistory-DateRemoval
Just a simple Python script which removes the date from ALL files created by Windows 10's FileHistory backup system.

## How do?
* Have Python 3.x installed.
* Download `filehistory.py`.
* Replace the string in between the citation marks of `rm_string = r" (2017_05_05 09_29_25 UTC)" ` with whatever you want to remove from all files (remember the whitespace in the begginning of the string).
* Run the script in e.g cmd.exe.
* Let the script run for however long it needs to complete the process.
* ???
* Be slightly satisfied and sigh at the inconvencience of Windows.

## Note
Python may say some files failed to be renamed, this is due to how Microsoft limits the names of files in its Windows system for some reason. If this is the case, just navigate to wherever the script points that error out.

## Warning
If you for some reason have files with a tilde (~) in the filename this script will remove all instances of the tilde character and replace it with a space.
