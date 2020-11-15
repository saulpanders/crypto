# Challenge 6:
# 	break repeating key XOR
#		THIS WORKS BUT IS SUPER UGLY AND COULD USE REFACTORING

from collections import Counter
from S5repeating_key_XOR import multi_byte_XOR
from S3single_byte_XOR import decipher_single_XOR
import base64
import itertools


def get_best_key_byte(ciphertext):
	return decipher_single_XOR(ciphertext)[0]

def retrieve_key(ciphertext):
	key = [get_best_key_byte(block)[0] for block in ciphertext]
	return bytes(key)

#TODO refactor for utils
#in: string (filename) ; out: string (decoded bytes)
def file_in(filename):
	with open(filename) as f:
		return base64.b64decode(f.read())

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


def break_multi_byte_XOR(data, max_key_length):
	keys = guess_key_size(data, max_key_length)
	key_sizes = [k[0] for k in keys[:5]]
	top_results = []
	for key_size in key_sizes:
		blocked_decoded_bytes = break_into_blocks(data,key_size)
		transposed_bytes = transpose_blocks(blocked_decoded_bytes)
		key =retrieve_key(transposed_bytes)
		plaintext = multi_byte_XOR(data, key)
		top_results.append((key, plaintext))
	return top_results


def main():
	filename = "challenge6.txt"
	decoded_bytes = file_in(filename)
	multi_xor_analysis = break_multi_byte_XOR(decoded_bytes, 40)
	print(multi_xor_analysis)



if __name__ == "__main__":
	main()