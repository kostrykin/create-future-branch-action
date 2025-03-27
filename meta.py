#!/usr/bin/env python

import argparse
import pathlib
import os
from datetime import date


parser = argparse.ArgumentParser()
parser.add_argument('--prefix', type=str, default='')
args = parser.parse_args()


today = date.today()
year = today.year % 2000

branch_name = f'{args.prefix}{year + 1}'
branch = f'future/{branch_name}'

print(f'branch-name={branch_name}')
print(f'branch={branch}')