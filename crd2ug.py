# ----------------------------------------------------------------------------
# A little utility to convert chopro-style files with embedded chord symbols 
# (e.g. "[Em]") to the multi-line format used by Ultimate Guitar.
#
# To use, specify the file to convert as a command line argument, 
# e.g. python crd2ug.py myfile.crd
# Or pipe it in, e.g. cat myfile.crd | python crd2ug.py
#
# In either case the processed lines are printed to stdout, so you will want 
# to redirect it into a file.
#
# Copyright (C) 2021 Christian Bolik
# ----------------------------------------------------------------------------

import fileinput

def process_line(line):
    crd_line = ""
    upd_line = line
    last_crd_len = 0
    while True:
        lbrk_index = line.find("[")
        if lbrk_index == -1:
            break
        rbrk_index = line.find("]")
        last_crd = line[lbrk_index + 1: rbrk_index]
        crd_line += " " * max(0 if len(crd_line) == 0 else 1, (lbrk_index - len(crd_line))) + last_crd
        upd_line = line[:lbrk_index] + line[rbrk_index + 1:]
        line = upd_line
    if len(crd_line) > 0:
        print(crd_line)
        if len(upd_line.rstrip()) > 0:
            print(upd_line, end="")
    else:
        print(upd_line, end="")

for line in fileinput.input():
    process_line(line)
