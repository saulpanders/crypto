# Challenge 11:
# 	An ECB/CBC detection oracle
#
#	 Write a function to generate a random AES key; that's just 16 random bytes.
#	Write a function that encrypts data under an unknown key --- that is, a function that generates a random key and encrypts under it. 
#
# 
from Crypto.Random import *
from Crypto.Cipher import AES
from S1_7AES_in_ECB import encrypt_AES_ECB, decrypt_AES_ECB
from S2_10implement_CBC_mode import encrypt_AES_CBC, decrypt_AES_CBC
from S1_8detect_AES_ECB import detect_AES_ECB
from random import *

def gen_random_AES_key():
	return get_random_bytes(AES.block_size)

def pad_random_bytes(data):
	return get_random_bytes(randint(5, 10)) + data + get_random_bytes(randint(5, 10))


def detect_AES_ECB_CBC(data):
	if (detect_AES_ECB(data)):
		return "ECB"
	else:
		return "CBC"


def AES_encryption_oracle(data):
	key = gen_random_AES_key()
	mode = randint(1,2)
	data = pad_random_bytes(data)
	iv = get_random_bytes(AES.block_size)

	# ECB mode
	if mode ==1 :
		return "ECB", encrypt_AES_ECB(data, key)
	#CBC mode
	else:
		return "CBC", encrypt_AES_CBC(data, key, iv)



def main():

	input_data = bytes([0]*64)
	#input_data = get_random_bytes(64)

	# Check that the detection method works correctly
	for i in range(100):
		encryption_used, ciphertext = AES_encryption_oracle(input_data)
		encryption_detected = detect_AES_ECB_CBC(ciphertext)
		if (encryption_used == encryption_detected):
			print("Match!" + " index " + str(i))


if __name__ == "__main__":
	main()



