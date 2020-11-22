# Util functions for crytopals

#in: string (filename) ; out: string (decoded bytes)
import base64 

def decode_base64_file(filename):
	with open(filename) as f:
		return base64.b64decode(f.read())



def main():
	print(decode_base64_file("1\\challenge6.txt"))

if __name__ == "__main__":
	main()