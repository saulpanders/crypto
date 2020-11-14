# Util functions for crytopals

#in: string (filename) ; out: string (decoded bytes)
import base64 

def file_in(filename):
	with open(filename) as f:
		return base64.b64decode(f.read())



def main():
	print(file_in("1\\challenge6.txt"))

if __name__ == "__main__":
	main()