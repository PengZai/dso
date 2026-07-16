

import re

input_file = "../build/bin/result.txt"
output_file = "dso.txt"

with open(input_file, "r") as fin, open(output_file, "w") as fout:
    for line in fin:
        # Strip leading/trailing whitespace, then collapse internal whitespace to one space
        cleaned = re.sub(r"\s+", " ", line.strip())
        fout.write(cleaned + "\n")