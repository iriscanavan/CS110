def occurance(seq, content):
	total_count = 0
	for bp in seq:
		if bp == content:
			total_count += 1
	return total_count

seq = "CBGAGE"
print("GC-content: " + str(float(occurance(seq, 'G') + occurance(seq, 'C')) / len(seq)))
