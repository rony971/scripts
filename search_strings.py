import sys
import os
import subprocess

"""
This script searches for specified strings in the current directory and its subdirectories using the `grep` command.

Usage:
    python search_strings.py string1 [string2 ... stringN]

Arguments:
    string1 [string2 ... stringN]: One or more strings to search for in the files.

Description:
    - The script takes one or more strings as command-line arguments.
    - For each string provided, it uses the `grep` command to search recursively (`-r`) in the current directory ('.').
    - The `-n` option is used to include line numbers in the output.
    - The `--color=always` option is used to highlight the matching strings in the output.
    - If no arguments are provided, the script prints a usage message and exits with a status code of 1.
"""


# Check if at least one argument is provided
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} string1 [string2 ... stringN]")
    sys.exit(1)

# Loop through each argument and search for it using grep
for search_string in sys.argv[1:]:
    print("========================================")
    print(f"Searching for: {search_string}")
    print("========================================")
    subprocess.run(['grep', '-rn', '--color=always', search_string, '.'])
    print()
