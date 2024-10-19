#!/usr/bin/python3
''' Code markdown2html.py script to take argument 2 strings:
    First argument is name of the Markdown file
    Second argument is name of output file
'''
import os
import sys

if __name__ == '__main__':
    # Check number of arguments
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]  # First argument: Markdown file
    output_file = sys.argv[2]     # Second argument: Output file name

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f'Missing {markdown_file}', file=sys.stderr)
        sys.exit(1)

    # If SUCCESS, exit with code 0
    sys.exit(0)
