#!/usr/bin/env python
#
import re, sys, argparse

parser = argparse.ArgumentParser(description = 'Prints lines NOT matching any patterns defined in the patterns file')
parser.add_argument('-p', '--patterns', metavar = 'PATTERNS_FILE', required = True, help = 'File containing patterns to filter (one per line)')
parser.add_argument('input', metavar = 'INPUT_FILE', help = 'File to process')
args = parser.parse_args()

patterns = open(args.patterns).read().split('\n') # Read from file
patterns = filter(None, patterns) # Remove any empty patterns
patterns = [re.compile(p) for p in patterns] # Compile patterns

# Determine if line should be kept
def keepLine(line):
  for pattern in patterns:
    if pattern.search(line):
      return False
  return True

# Process input file
with open(args.input) as input:
  for line in input:
    if keepLine(line):
      print line,
