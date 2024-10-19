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

    # Function to check if the provided Markdown file exists
    def check_markdown_file_exists(markdown_file):
    return os.path.exists(markdown_file)

    # Function to convert Markdown headings to HTML
    def convert_markdown_to_html(markdown_file):
    html_content = []  # List to store HTML lines
    with open(markdown_file, 'r') as file:
        for line in file:
            line = line.rstrip()  # Remove trailing whitespace
            if line.startswith('#'):
                heading_level = line.count('#')  # Count the number of '#' to determine the heading level
                heading_text = line[heading_level:].strip()  # Get the heading text
                # Generate the corresponding HTML heading
                html_content.append(f'<h{heading_level}>{heading_text}</h{heading_level}>')
                return '\n'.join(html_content)  # Join the HTML lines into a single string

    # Check number of arguments
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

        markdown_file = sys.argv[1]  # First argument: Markdown file
        output_file = sys.argv[2]     # Second argument: Output file name

    # Check if the Markdown file exists
    if not check_markdown_file_exists(markdown_file):
    print(f'Missing {markdown_file}', file=sys.stderr)
    sys.exit(1)

    # Convert the Markdown file to HTML
    html_output = convert_markdown_to_html(markdown_file)

    # Write the HTML output to the specified output file
    with open(output_file, 'w') as f:
    f.write(html_output)

    # If SUCCESS, exit with code 0
    sys.exit(0)
