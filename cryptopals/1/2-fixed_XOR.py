# Challenge 2:
# 	Fixed XOR
#	
#	take two equal-sized buffers and returns XOR combination
#	Input: 1c0111001f010100061a024b53535009181c (need to hex decode)
#			686974207468652062756c6c277320657965
#	output: 746865206b696420646f6e277420706c6179

# in: string (hex), string(hex) ; out: string (hex)
def fixed_size_XOR(buffer_1, buffer_2):
	b1_bytes = bytes.fromhex(buffer_1) 
	b2_bytes = bytes.fromhex(buffer_2)
	xor_result = bytes([x ^ y for x,y in zip(b1_bytes, b2_bytes)])
	return bytes.hex(xor_result)

b1 = "1c0111001f010100061a024b53535009181c"
b2 = "686974207468652062756c6c277320657965"
print(fixed_size_XOR(b1,b2))