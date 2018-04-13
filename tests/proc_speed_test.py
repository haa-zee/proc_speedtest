#!/usr/bin/env python3

from __future__ import print_function
from glob import glob
import sys


n=0
e=0

for j in range(10000):
	for g in glob("/proc/[0-9]*/stat"):
		try:
			with open(g,"r") as f:
				s=f.readline()
				n+=1
		except Exception:
			e+=1

print("Count: ",n)
print("Error: ",e)


