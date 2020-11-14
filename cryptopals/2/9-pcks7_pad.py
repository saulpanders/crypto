# Challenge 9:
#
# Implement PKCS#7 padding
# pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. 
#
#

def pkcs7_pad_block(block, pad_length):
	if(len(block) == pad_length):
		return block
	if(len(block) > pad_length):
		raise Exception("Error, pad size less than overall block length")
		return block
	pad_index = pad_length - len(block) % pad_length
	return block + bytes([pad_index] * pad_index)



def check_pcks7_pad(binary_data):
	padding = binary_data[-binary_data[-1]:]
	return all(padding[i] == len(padding) for i in range(0, len(padding)))

def unpad_pcks7_block(block):
	if(len(block) == 0):
		raise Exception("The input data must contain at least one byte")
	if not check_pcks7_pad(block):
		return block
	pad_len = block[-1]
	return block[:-pad_len]

def main():
	test_data = b'YELLOW SUBMARINE'
	pad_length = 20
	pad = pkcs7_pad_block(test_data,pad_length)
	print(check_pcks7_pad(test_data))
	print(check_pcks7_pad(pad))
	print(unpad_pcks7_block(pad))

if __name__ == "__main__":
	main()
