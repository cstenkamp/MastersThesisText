"""
This script takes a file with acronyms in the form of
"Coordinated Universal Time (UTC)"
and prints them into the format for the LaTeX package gloassaries
"\newacronym{utc}{UTC}{Coordinated Universal Time}".

Usage:
    run $ python acronyms2glossaries <file_with_acronyms>
    in your shell. If no file is supplied, acornyms.txt is assumed as 
    default.
"""

import sys
import re

try:
    filename = sys.argv[1]
except IndexError:
    filename = 'acronyms.txt'

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
        
for entry in glossary_entries:
    print(entry)
    
