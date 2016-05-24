#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
# Gets a list of the absolute paths of all files that meet the naming criteria
def getAbsolutePaths(args):
  paths = []; # Absolute paths of all the files that meet the '__w__' naming criteria

  # Get all qualifying names
  for arg in args:
    filesInDir = os.listdir(arg)
    for file in filesInDir:
      fileName = re.search(r'\w*(__\w+__)\w*\.', file)
      if fileName:
        absoluteFilePath = os.path.abspath(os.path.join(arg, file))
        paths.append(absoluteFilePath)

  return paths

# Copy files given to directory todir
def copyFiles(absolutePaths, todir):
  if not os.path.exists(todir):
    os.mkdir(todir)

  for path in absolutePaths:
      shutil.copy(path, todir)

  return

# Make a zip file of all the files given in absolutePaths
def makeZipFile(absolutePaths, tozip):
  cmd = 'zip -j ' + tozip + ' ' + ' '.join(absolutePaths)
  print 'Command to run: ' + cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status: # Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(1)

  print output

  return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  absolutePaths = getAbsolutePaths(args)

  if todir != '': # Copying files to directory
    copyFiles(absolutePaths, todir)
  if tozip != '': # Making a zip file
    makeZipFile(absolutePaths, tozip)
  else: # Simplest case, just print
    print absolutePaths

  
if __name__ == "__main__":
  main()
