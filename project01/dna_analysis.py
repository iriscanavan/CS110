# Iris Canavan, Section 3

# This project is based on Michaels Ernt's assignment on DNA analysis

import sys

def occurrence(seq, nucleotide):
	count = 0
	for bp in seq:
		if bp == nucleotide:
			count += 1
	return count

def classification(gc_content):
	if gc_content > 0.60:
		return "High GC content"
	elif gc_content < 0.40:
		return "Low GC content"
	else:
		return "Moderate GC content"

if len(sys.argv) < 2:
	print("invalid arguments")
	sys.exit(-1)

fpath = sys.argv[1]
inputfile = open(fpath)

seq = ""
linenum = 0

for line in inputfile:
	linenum = linenum + 1
	if linenum % 4 == 2:
		line = line.rstrip()
		seq += line

g_count = (occurrence(seq, 'G'))
c_count = (occurrence(seq, 'C'))
a_count = (occurrence(seq, 'A'))
t_count = (occurrence(seq, 'T'))

sum_count = g_count + c_count + a_count + t_count
gc_content = (g_count + c_count) / sum_count
at_content = (a_count + t_count) / sum_count

total_count = len(seq)

at_gc_ratio = ((a_count + t_count) / (g_count + c_count))

# problem 1b
print("GC-content:", round(gc_content, 12))

# problem 2a
print("AT-content:", round(at_content, 12))

# problem 2b
print("G count:", g_count)
print("C count:", c_count)
print("A count:", a_count)
print("T count:", t_count)

# problem 2c
print("Sum count:", sum_count)
print("Total count:", total_count)
print("Seq length:", len(seq))

# problem 2d
print("AT/GC ratio:", round(at_gc_ratio, 12))

# problem 2e
print("GC Classification:", classification(gc_content))
