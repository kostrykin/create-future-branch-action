#!/usr/bin/env python

import pathlib
import os
from datetime import date


def expand(today):
    year = today.year % 2000
    if 4 <= today.month <= 8:
        prefix = 'ss'
    else:
        prefix = 'ws'

    branch_name = f'{prefix}{year + 1}'
    branch = f'future/{branch_name}'

    return {
        'branch-name': branch_name,
        'branch': branch,
    }


if __name__ == '__main__':
    today = date.today()
    data = expand(today)
    for key, value in data.items():
        print(f'{key}={value}')