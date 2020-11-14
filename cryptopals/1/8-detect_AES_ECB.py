# Challenge 8:
# 	AES in ECB mode
#	
#	in challenge8.txt are a bunch of hex-encoded ciphertexts.
#
#	One of them has been encrypted with ECB. Detect it
#	Idea: break ciphertext into ECB blocks, test all pairs of blocks for matches (n(n-1))/2) possible pairs


def calculate_block_freq(ciphertext):
	block_list = [ciphertext[i:i + 16] for i in range(0, len(ciphertext), 16)]
	block_summary = {x:block_list.count(x) for x in block_list}
	return block_summary

def detect_block_match(analysis):
	line_match = 0
	for elem in analysis.items():
		if elem[1] > 1:
			line_match +=1
	return line_match

def detect_AES_ECB(ciphertext):
	line_block_analysis = calculate_block_freq(bytes.fromhex(ciphertext))
	num_block_matches = detect_block_match(line_block_analysis)
	if(num_block_matches > 0):
		print(ciphertext)
		print(line_block_analysis)

def main():
	filename = "challenge8.txt"
	with open(filename) as f:
		for line in f:
			detect_AES_ECB(line)


if __name__ == "__main__":
	main()
