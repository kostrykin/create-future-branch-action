#!/usr/bin/env python

from datetime import date
import os
import pathlib


prefix = os.environ['PREFIX']
init = os.environ['INIT']

today  = date.today()
year   = today.year % 2000
branch = f'future/{prefix}{year + 1}'

os.system(f'git checkout -b {branch}')
#if len(init) > 0:
#    os.system(f'{init} "{branch}"')

print(branch)