# Challenge 5:
# 	Implement repeating key XOR cipher (vignere cipher)
#		
# 	encrypt: "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
#
#	with key "ICE"
#	result should be:
#		0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

#in: byte string ciphertext/plaintext, byte string key ; out: byte string plaintext/ciphertext
def multi_byte_XOR(plain,key):
	return bytes([ x ^ key[ i% len(key)] for i,x in enumerate(plain)])



def main():
	plaintext = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	key = b"ICE"
	print(bytes.hex(multi_byte_XOR(plaintext,key)))


if __name__ == "__main__":
	main()