#!/usr/bin/env python

import fileinput
import sys

firstline = True

for line in fileinput.input():
    if firstline:
      firstline = False
      sys.stdout.write('[')
    else:
      sys.stdout.write(',\n')

    sys.stdout.write(line.strip('\n'))

if firstline is False:
  sys.stdout.write(']\n')
