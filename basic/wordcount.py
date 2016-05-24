#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# This function takes in a filename and then proceeds to open the file,
# and build a word/count dictionary of the file's contents.
def build_dict(filename):
  wordCountDict = {}

  f = open(filename, 'rU')

  for line in f:
    for word in line.split():
      if word.lower() in wordCountDict:
        wordCountDict[word.lower()] += 1
      else:
        wordCountDict[word.lower()] = 1
                   
  f.close()

  return wordCountDict

# Prints out a list of all words present in the file and how many times each word occurs,
# sorted alphabetically
def print_words(filename):
  wordDict = build_dict(filename)

  for key in sorted(wordDict.keys()):
    print key, wordDict[key]

  return

# Prints out a list of the top 20 most common words in the file
def print_top(filename):
  wordDict = build_dict(filename)
  flag = 1;

  for key in sorted(wordDict, key=wordDict.get, reverse=True):
    if flag > 20:
      break
    else:
      print key, wordDict[key]
      flag += 1

  return


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
