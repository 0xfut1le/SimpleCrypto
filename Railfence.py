from base import Cipher

class Railfence(Cipher):
    def __init__(self, message=None, key=None, encrypt=False, verbose=False):
        """
            The Railfence cipher is a fun cipher to encounter during CTF's.
            Although, for lengthier messages, calculating by hand can try
            a person's patience. In essence, to encrypt or decyrpt a railfence
            cipher, you first need to determine the key size and depending on
            the key size, you write the ciphertext in zig-zags across that many
            rows. So, for example, a key with size of 3 would produce 3 rows with
            as many columns as there are characters in the message.
        """
        self.message    = message
        self.key        = key
        self.encrypt    = encrypt
        self.verbose    = verbose 
        self.ciphertext = ""
        self.plaintext  = ""

    def __repr__(self):
        if self.key <= 0:
            raise ValueError('Invalid Key: %d \n Key must be greater than zero!' % self.key)
        if self.encrypt:
            return self.encrypt_railfence()
        else:
            return self.decrypt_railfence()
    
    def encrypt_railfence(self):
        """
            :params message string to encrypt
            :params key how many rows to span the message over

            :returns ciphertext
        """
        self.ciphertext = ''.join(self.buildfence(self.message, self.key))
        return self.ciphertext

    def decrypt_railfence(self):
        """
            :params ciphertext Message to decrypt
            :params key used to encrypt message

            :returns plaintext
        """
        key = self.key
        message_len = len(self.message)
        message = self.message
        fence_range = range(message_len)
        pos = self.buildfence(fence_range, key)
        

        self.plaintext = ''.join(message[pos.index(i)] for i in fence_range)
        return self.plaintext

    def buildfence(self, chars, key):
        """
            :params chars string to encrypt
            :key number of rows to write the message over

            returns list of values.

            This function is the workhorse of the railfence cipher.
            First we initialize a nested list filled with None type of
            width = len(message) and height = key.
            Rails generates the list of where to place each character.
            For example, a message of length = 19 and key = 8, returns
            rails = [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]

            Next we loop through the fence list and for each value in 
            rails, we place a character. When encrypting, this means
            each character in the message. But when decrypting, we 
            are simply returning the **index values** where each 
            character from the ciphertext is placed in the fence 
            nested list. 
        """
        # initialize the fence nested list with None values for
        # width = len(message) and height range(key)
        fence = [[None] * len(chars) for n in range(key)]
        rails = list(range(key - 1)) + list(range(key - 1, 0, -1))
        
        for n, x in enumerate(chars):
            fence[rails[n % len(rails)]][n] = x
        return [c for rail in fence for c in rail if c is not None]

'''
message = "Yeti Another Cipher"
Test = Railfence(message=message, key=8, encrypt=True)
print('Encrypt Railfence : %s' % Test)
dec_message = "YieCpt hire erAhnto"
Test2 = Railfence(message=dec_message, key=8, encrypt=False)
print('Decrypt Railfence : %s' % Test2)
'''