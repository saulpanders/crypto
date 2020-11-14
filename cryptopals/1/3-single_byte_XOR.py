# Challenge 3:
# 	Single-byte XOR cipher
#	
#	hex encoded input has been XOR'd against a single character. Find the key, decrypt the message. 
#	Input: 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736 (need to hex decode)
#			
#	come up with a way to "score englishness" of plaintext (fitness)

from collections import Counter

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
def brute_single_byte_XOR(hex_string):
	hex_bytes = bytes.fromhex(hex_string)
	brute_results = {}
	for i in range(256):
		brute_results[i] = bytes([x ^ i for x in hex_bytes])
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

def decipher(hex_string):
	xor_brute_matrix  = compute_fitness_quotient(brute_single_byte_XOR(hex_string))
	sorted_by_fitness = sorted(xor_brute_matrix.items(), key=lambda tup: tup[1][1])
	print("Top 5 results (english)")
	for i in range(5):
		print(i+1, ": ",sorted_by_fitness[i])

ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
decipher(ciphertext)