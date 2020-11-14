# Challenge 1:
# 	Convert hex to base64
#	
#	input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d 
#	output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#
#	NOTE: Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing. 

import base64

# in: string (hex) ; out string (base64)
def hex_to_bs4(hex_string):
	hex_bytes = bytes.fromhex(hex_string) 
	base64_bytes = base64.b64encode(hex_bytes) 
	return base64_bytes

test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d" 
print(hex_to_bs4(test))