# Challenge 2:
# 	Fixed XOR
#	
#	take two equal-sized buffers and returns XOR combination
#	Input: 1c0111001f010100061a024b53535009181c (need to hex decode)
#			686974207468652062756c6c277320657965
#	output: 746865206b696420646f6e277420706c6179

# in: string (hex), string(hex) ; out: string (hex)
def fixed_size_XOR(b1, b2):
	if (len(b1) != len(b2)):
		raise
	xor = bytes([x ^ y for x,y in zip(b1, b2)])
	return xor

def main():
	b1 = "1c0111001f010100061a024b53535009181c"
	b2 = "686974207468652062756c6c277320657965"
	b1_bytes = bytes.fromhex(b1) 
	b2_bytes = bytes.fromhex(b2)
	xor_results = fixed_size_XOR(b1_bytes,b2_bytes)
	print(bytes.hex(xor_results))


if __name__ == "__main__":
	main()