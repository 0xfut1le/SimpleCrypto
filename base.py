import re

class Cipher(object):
    def encrypt(self, message):
        return message
    
    def decrypt(self, plaintext):
        return plaintext

    def alpha_to_int(self, ch):
        char_val = ord(ch)

        if char_val >= 91 and char_val <= 96:
            return char_val
        else:
            return char_val - 65 

    def int_to_alpha(self, digit):
        return chr(digit + 65)
        
    def remove_punctuation(self, message, filter='[^a-zA-Z0-9_=()]'):
        return re.sub(filter, '', message)  
