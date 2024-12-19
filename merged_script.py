import configparser
import argparse
import os
import subprocess
import sys

def find_section_and_rank_for_elements(file_path, elements):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(file_path)
    
    results = {}
    for element in elements:
        found = False
        for section in config.sections():
            for item in config[section]:
                if element in item:
                    rank = list(config[section]).index(item)
                    results[element] = (section, rank)
                    found = True
                    break
            if found:
                break
        if not found:
            results[element] = (None, None)
    return results

def search_strings(strings):
    for search_string in strings:
        print("========================================")
        print(f"Searching for: {search_string}")
        print("========================================")
        subprocess.run(['grep', '-rn', '--color=always', search_string, '.'])
        print()

def main():
    parser = argparse.ArgumentParser(description='Search for strings and find section and rank of elements in INI files.')
    parser.add_argument('elements', nargs='*', help='List of elements to search for')
    parser.add_argument('--file', type=str, help='File containing list of elements to search for')
    parser.add_argument('--search', nargs='*', help='List of strings to search for in files')
    args = parser.parse_args()

    elements = args.elements
    if args.file:
        with open(args.file, 'r') as f:
            file_elements = [line.strip() for line in f.readlines()]
            elements.extend(file_elements)

    if elements:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        ini_files = [f for f in os.listdir(script_dir) if f.endswith('.ini')]

        for ini_file in ini_files:
            file_path = os.path.join(script_dir, ini_file)
            print(f"Processing file: {file_path}")
            results = find_section_and_rank_for_elements(file_path, elements)

            for element, (section, rank) in results.items():
                if section:
                    print(f"The element '{element}' is in the section: [{section}] at rank {rank}")
                else:
                    print(f"The element '{element}' was not found in any section.")
            print()

    if args.search:
        search_strings(args.search)

if __name__ == "__main__":
    main()