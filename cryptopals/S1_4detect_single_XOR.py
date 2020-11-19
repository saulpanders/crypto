# Challenge 4:
# 	Detecting a single-byte XOR cipher
#	
# One of the 60-character strings in challenge4.txt has been encrypted by single-character XOR. 
# Find it
#
#TODO refactor for modularity

from collections import Counter
from S1_3single_byte_XOR import brute_single_byte_XOR, compute_fitness_quotient, decipher_single_XOR


# in: string (name of ciphertext); out: tuple (best line match)
def parse_file(filename):
	with open(filename) as f:
		ciphertext_results = [decipher_single_XOR(bytes.fromhex(x))[0] for x in f]
		sorted_by_fitness = sorted(ciphertext_results, key=lambda tup: tup[1][1])
		print(sorted_by_fitness[0])

def main():
	filename = "challenge4.txt"
	parse_file(filename)


if __name__ == "__main__":
	main()