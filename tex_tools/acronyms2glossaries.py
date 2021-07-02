"""
This script takes a file with acronyms in the form of
"Coordinated Universal Time (UTC)"
and prints them into the format for the LaTeX package gloassaries
"\newacronym{utc}{UTC}{Coordinated Universal Time}".

Usage:
    run $ python acronyms2glossaries.py <file_with_acronyms>
    in your shell. If no file is supplied, acronyms.txt is assumed as 
    default.
"""
from os.path import join, isdir, isfile, abspath, dirname, splitext, basename, split
import re
import argparse


def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='acronyms.txt', help='Name of the you save your acronyms (defaults to acronyms.txt)')
    parser.add_argument('-w', '--writeout', default=False, help='If you want to write out back to thesis.text', action='store_true')
    return parser.parse_args()


def main():
    args = parse_command_line_args()
    glossary_entries = get_glossary(args.filename)

    if args.writeout:
        START_TXT = "% START Acronym definitions"
        END_TXT = "% END Acronym definitions"
        write_file = join(dirname(__file__), "..", 'thesis.tex')
        with open(write_file, "r") as wfile:
            # lines = [i.strip("\n") for i in wfile.readlines()]
            lines = "".join(wfile.readlines())
        assert lines.find(START_TXT) and lines.find(END_TXT), f"You deleted the lines {START_TXT} and {END_TXT}!"
        assert lines.find(START_TXT) < lines.find(END_TXT), f"You mixed up the lines {START_TXT} and {END_TXT}!"
        pre = lines[:lines.find(START_TXT)-1]
        between = lines[lines.find(START_TXT)+len(START_TXT)+1:]
        between = between[:between.find(END_TXT)-1]
        end = lines[lines.find(END_TXT)+len(END_TXT)+1:]
        txt = pre+f"\n{START_TXT}\n"+"\n".join(glossary_entries)+f"\n{END_TXT}\n"+end
        with open(write_file, "w") as wfile:
            wfile.write(txt)
    else:
        for entry in glossary_entries:
            print(entry)
        

def get_glossary(filename):
    glossary_entries = []
    glossaries_format = '\\newacronym{{{}}}{{{}}}{{{}}}'
    acronym_regex = re.compile('(.+?)\s\((.+)\)')
    with open(filename, 'r') as acronym_file:
        for line in acronym_file:
            # Search the line for the acronym and its abbreviation.
            parsed = acronym_regex.match(line)
            if parsed:
                description = parsed.group(1)
                abbreviation = parsed.group(2)
                glossary_entry = glossaries_format.format(
                                    abbreviation.lower(),
                                    abbreviation,
                                    description,
                                )
                glossary_entries.append(glossary_entry)
            else: 
                raise ValueError("%s is malformed" % line)
    return glossary_entries




    
    
if __name__ == '__main__':
    main()
   
