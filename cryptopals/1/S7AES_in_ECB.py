# Challenge 7:
# 	AES in ECB mode
#		
# The Base64-encoded content in challenge7.txt has been encrypted via AES-128 in ECB mode under the key: "YELLOW SUBMARINE"
#	note: (case-sensitive, without the quotes; exactly 16 characters)
#
#	decrypt using code
import base64
from Crypto.Cipher import AES



def file_in(filename):
	with open(filename) as f:
		return base64.b64decode(f.read())



#in: byte array (decoded bytes), bytearray (key) ; out: bytearray (decrypted) 
def decrypt_AES_ECB(byte_stream, key):
	 cipher = AES.new(key, AES.MODE_ECB)
	 return cipher.decrypt(byte_stream)

def main():
	filename = "challenge7.txt"
	key = b'YELLOW SUBMARINE'
	decoded_bytes = file_in(filename)
	decrypted_bytes = decrypt_AES_ECB(decoded_bytes, key)
	print(decrypted_bytes)



if __name__ == "__main__":
	main()


