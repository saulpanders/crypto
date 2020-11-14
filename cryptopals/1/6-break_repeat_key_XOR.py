# Challenge 6:
# 	break repeating key XOR
#		THIS WORKS BUT IS SUPER UGLY AND COULD USE REFACTORING

import base64
from collections import Counter
import itertools


occurance_english = {
    'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
    'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
    'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
    'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
    'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
    'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
    'y': 1.9913847,    'z': 0.0746517
}

# in: string (hexidecimal); out: dict with {byte: decrypt_attempt}
def brute_single_byte_XOR(ciphertext):
	brute_results = {}
	for i in range(256):
		brute_results[i] = bytes([x ^ i for x in ciphertext])
	return brute_results


#note: a low fitness score means closer to english
# in: out: dict with {byte: decrypt_attempt}; out: dict with {byte: (decrypt_attempt,fitness_score)}
def compute_fitness_quotient(brute_results):
	dist_english = list(occurance_english.values())
	for key in brute_results:
		text_letter_count = Counter(brute_results[key])
		dist_text = [(text_letter_count.get(ord(ch), 0) * 100) / len(brute_results[key]) for ch in occurance_english]
		fitness = sum([abs(a - b) for a, b in zip(dist_english, dist_text)]) / len(dist_text)
		brute_results[key] = (brute_results[key], fitness)
	return brute_results

def get_best_key_byte(ciphertext):
	xor_brute_matrix  = compute_fitness_quotient(brute_single_byte_XOR(ciphertext))
	sorted_by_fitness = sorted(xor_brute_matrix.items(), key=lambda tup: tup[1][1])
	return sorted_by_fitness[0]

def retrieve_key(ciphertext):
	key = [get_best_key_byte(block)[0] for block in ciphertext]
	return bytes(key)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ check above for bugs

#in: string (filename) ; out: string (decoded bytes)
def file_in(filename):
	with open(filename) as f:
		return base64.b64decode(f.read())

#this works!
#in: byte string, byte string; out: int (hamming distance -> 0 == strings are the same)
def hamming_distance(x,y):
	d = 0
	res = bytes([x^y for x,y in zip(x,y)])
	for x in res:
		d = d + bin(x).count('1')
	return d

def normalized_hamming_distance(x, k):
    pairs = list(itertools.combinations(x, 2))
    scores = [hamming_distance(p[0], p[1])/float(k) for p in pairs][0:6]
    return sum(scores) / len(scores)

#in: byte array, int ; out: list[tup] -> list of tuples (key_size, hamming_distance_between_block1_and_block2)
def guess_key_size(ciphertext,max_key_length):
	block_list = []
	key_hist = {}
	ciphertext = bytearray(ciphertext)
	for x in range(2, max_key_length + 1):
		if len(ciphertext) % x != 0:
			pad = bytearray(x)
			for b in pad:
				ciphertext.append(b)
		try:
			block_list = [ciphertext[i:i + x] for i in range(0, len(ciphertext), x)]
		except:
			raise
		key_hist[x] = normalized_hamming_distance(block_list, x)

	#sort by hamming dist before we return
	return sorted(key_hist.items(), key=lambda tup: tup[1])

def break_into_blocks(ciphertext, key_size):
	blocks = [ciphertext[i:i + key_size] for i in range(0, len(ciphertext), key_size)]

	#padding last block to fit key len
	if(len(ciphertext) % key_size) != 0:
		pad_len = key_size - (len(ciphertext) % key_size)
		padded_block = [blocks[-1]] + ([bytes(pad_len)])
		blocks[-1] = b''.join(padded_block)

	return blocks

def transpose_blocks(ciphertext):
	t_blocks = list(zip(*ciphertext))
	t_blocks = [ b"".join(bytes([x]) for x in y) for y in t_blocks]
	return t_blocks

def decrypt_multi_byte_XOR(plain,key):
	return bytes([ x ^ key[ i% len(key)] for i,x in enumerate(plain)])


def main():
	filename = "challenge6.txt"
	decoded_bytes = file_in(filename)
	keys = guess_key_size(decoded_bytes, 40)
	key_sizes = [k[0] for k in keys[:5]]
	for key_size in key_sizes:
		blocked_decoded_bytes = break_into_blocks(decoded_bytes,key_size)
		transposed_bytes = transpose_blocks(blocked_decoded_bytes)
		key =retrieve_key(transposed_bytes)
		plaintext = decrypt_multi_byte_XOR(decoded_bytes, key)
		print(key)
		print(plaintext)



if __name__ == "__main__":
	main()