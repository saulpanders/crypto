# Challenge 10:
# 	Implement CBC mode
#
#  "challenge10.txt" is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c) 
# Idea: take ECB mode function (convert to decrypt) & combine with fixed buf XOR to hack CBC together
# 

from Crypto.Cipher import AES
from S1_2fixed_XOR import fixed_size_XOR
from S1_7AES_in_ECB import encrypt_AES_ECB, decrypt_AES_ECB
from utils import decode_base64_file

def encrypt_AES_CBC(data, key, iv):
	cipher = b""
	prev_block = iv
	for i in range(0,len(data), AES.block_size):
		cur_block = data[i: i + AES.block_size]
		xor_result = fixed_size_XOR(cur_block, prev_block)
		encrypt_block = encrypt_AES_ECB(xor_result, key)
		prev_block = encrypt_block
		cipher += encrypt_block

	return cipher

def decrypt_AES_CBC(data, key, iv):
	plain = b""
	prev_block = iv
	for i in range(0,len(data), AES.block_size):
		cur_block = data[i: i + AES.block_size]
		decypt_block = decrypt_AES_ECB(cur_block, key)
		xor_result = fixed_size_XOR(decypt_block, prev_block)
		prev_block = cur_block
		plain +=xor_result
	return plain



def main():
	filename = "challenge10.txt"
	key = b'YELLOW SUBMARINE'
	iv  = b'\x00' * AES.block_size
	decoded_bytes = decode_base64_file(filename)
	plain = decrypt_AES_CBC(decoded_bytes,key,iv)
	cipher = encrypt_AES_CBC(plain, key, iv)
	plain_2 = decrypt_AES_CBC(cipher, key, iv)
	print(plain)
	print(cipher)
	print(plain_2)


if __name__ == "__main__":
	main()