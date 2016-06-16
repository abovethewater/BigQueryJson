#!/usr/bin/env python

import fileinput
import sys

bracketOpen = False
isAlreadyJSON = False

for line in fileinput.input():

  if fileinput.isfirstline():
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
