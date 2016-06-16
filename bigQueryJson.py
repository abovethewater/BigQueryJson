#!/usr/bin/env python

import fileinput
import sys

firstLine = True
bracketOpen = False
isAlreadyJSON = False

for line in fileinput.input():

  line = line.strip()

  if len(line) is 0:
    continue

  if firstLine is True:
    firstLine = False
    if line[0] != '[':
      bracketOpen = True
      sys.stdout.write('[')
    else:
      isAlreadyJSON = True
  else:
    if isAlreadyJSON is False:
      sys.stdout.write(',')
    sys.stdout.write('\n')

  sys.stdout.write(line.strip('\n'))

if bracketOpen is True:
  sys.stdout.write(']')

sys.stdout.write('\n')

sys.stdout.flush()
