#!/usr/bin/env python

import pathlib
import os
from datetime import date


def expand(today):
    year = today.year % 2000
    if 4 <= today.month <= 8:
        prefix = 'ss'
        year += 1
    else:
        prefix = 'ws'
        if today.month > 8:
            year += 1

    branch_name = f'{prefix}{year}'
    branch = f'future/{branch_name}'
    branch_description = f'{prefix.upper()} {year}' + (f'/{year + 1}' if prefix == 'ws' else '')

    return {
        'branch': branch,
        'branch-name': branch_name,
        'branch-description': branch_description,
    }


if __name__ == '__main__':
    today = date.today()
    data = expand(today)
    for key, value in data.items():
        print(f'{key}={value}')