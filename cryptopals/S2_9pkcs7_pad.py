# Challenge 9:
#
# Implement PKCS#7 padding
# pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. 
#
#

def pkcs7_pad_block(block, pad_length):
	if(len(block) == pad_length):
		return block
	else:
		pad_index = pad_length - len(block) % pad_length
		return block + bytes([pad_index] * pad_index)



def check_pkcs7_pad(binary_data):
	padding = binary_data[-binary_data[-1]:]
	return all(padding[i] == len(padding) for i in range(0, len(padding)))

def pkcs7_unpad_block(block):
	if not check_pkcs7_pad(block):
		return block
	else:
		pad_len = block[-1]
		return block[:-pad_len]

def main():
	test_data = b'YELLOW SUBMARINE'
	t2 = b"a"
	pad_length = 20
	pad = pkcs7_pad_block(t2,pad_length)
	print(pad)
	print(check_pkcs7_pad(test_data))
	print(check_pkcs7_pad(pad))
	print(pkcs7_unpad_block(pad))

if __name__ == "__main__":
	main()
