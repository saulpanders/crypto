# Challenge 8:
# 	AES in ECB mode
#	
#	in challenge8.txt are a bunch of hex-encoded ciphertexts.
#
#	One of them has been encrypted with ECB. Detect it
#	Idea: break ciphertext into ECB blocks, test all pairs of blocks for matches (n(n-1))/2) possible pairs

#  in: ciphertext (string) ; out: dict summarizing results for each blocks freq in file {block: block_freq}
def calculate_block_freq(ciphertext):
	block_list = [ciphertext[i:i + 16] for i in range(0, len(ciphertext), 16)]
	block_summary = {x:block_list.count(x) for x in block_list}
	return block_summary


# in: block analysis dict (see above); out: # of matching lines in a block
def detect_block_match(block_summary):
	line_match = 0
	for elem in block_summary.items():
		if elem[1] > 1:
			line_match +=1
	return line_match

# in: ciphertext string ; out: AES_ECB cipher string + block analysis || False
def detect_AES_ECB(ciphertext):
	line_block_analysis = calculate_block_freq(ciphertext)
	num_block_matches = detect_block_match(line_block_analysis)
	if(num_block_matches > 0):
		return (ciphertext, line_block_analysis)
	else:
		return False


def main():
	filename = "challenge8.txt"
	with open(filename) as f:
		for line in f:
			byte_str = bytes.fromhex(line)
			if(detect_AES_ECB(line)):
				print(detect_AES_ECB(line))


if __name__ == "__main__":
	main()
