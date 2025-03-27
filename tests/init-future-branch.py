import argparse

parser = argparse.ArgumentParser()
parser.add_argument('branch')
args = parser.parse_args()

with open('example/initialized.txt', 'w') as fp:
    print(f'Initialized branch: "{args.branch}"', file=fp)