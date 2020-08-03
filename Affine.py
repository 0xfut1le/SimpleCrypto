from base import Cipher
import string

class Affine(Cipher):
    def __init__(self, message, key_1=None, key_2=None, encrypt=False, atbash=False):
        """
            Affine takes in two key values A and B which are applied in the formula
            E(x) = (ax + b) % m to where x is the letter and b is the amount to shift.
            To decrypt the message, E(x) = inv(a)(x - b) % m.
        """
        self.message = message
        self.key_1      = key_1
        self.key_2      = key_2
        self.encrypt    = encrypt
        self.atbash     = atbash
        self.ciphertext = ""
        self.plaintext  = ""
        self.alpha      = string.ascii_letters + string.digits

    def __repr__(self):
        if self.atbash:
            return self.calc_atbash()
        else:
            if self.encrypt and not self.atbash:
                return self.encrypt_affine()
            else:
                return self.decrypt_affine()

    def calc_atbash(self):
        """
            AtBash is basically an Affine cipher where a = b = (m - 1). Here we utilize
            the String library to first make a reversed alphabet which we can use to
            translate the ciphertext to the plaintext with the .translate(DECODE_TABLE)
            call. Since there is only one key to the cipher, the same process that is
            used to encrypt the message can be applied to the same message to decrypt it.
        """
        DECODE_TABLE = str.maketrans(
            string.ascii_letters,
            ''.join(reversed(string.ascii_letters)))
        self.plaintext = str((self.message).translate(DECODE_TABLE))
        return str(self.plaintext)

    def encrypt_affine(self):
        """
            :params key_1
            :params key_2
            :return ciphertext

            This function takes the two key values and applies the shift,
            (ax + b) % 62 to each letter and appends it to the ciphertext
            string.
        """
        key_1 = self.key_1
        key_2 = self.key_2
        coprime = self.gen_coprime() # [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        message = self.message
        alpha_len = len(self.alpha)
      
        if key_1 not in coprime:
            raise ValueError('key_1 value [%d] is not a coprime of %d!' % (key_1 ,alpha_len))
        else:
            for ch in message:
                if ch in self.alpha:
                    letter_pos = (self.alpha).find(ch)
                    letter = self.alpha[(key_1 * letter_pos + key_2) % alpha_len] # E(x) = (ax + b) % m
                    self.ciphertext += letter
                    """
                    Used for debugging:
                    print('%s : %s' % (ch, letter))
                    """
                else:
                    self.ciphertext += ch
                    """ 
                    Used for debugging:
                    print('Symbol : %s' % ch)
                    """
            return self.ciphertext

    def decrypt_affine(self):
        """
            :params key_1
            :params key_2
            :return plaintext

            To decrypt an affine cipher, we take the inverse value of key_1 and multiply it
            to the current character - key_2 before modding it by the alpha_len.
            i.e a^-1(x - b) % 62. If a character is not part of the standard alphabet,
            we simply append that to the plaintext (assuming symbols, punctuation, etc)
        """
        key_1 = self.key_1
        key_2 = self.key_2
        alpha_len = len(self.alpha)
        inv_a = pow(key_1, -1, alpha_len)
        coprime = self.gen_coprime()
        
        message = self.message
        
        # print('key_1 : %d; Inverse A : %d' % (key_1, inv_a))

        if key_1 not in coprime:
            raise ValueError('key_1 value is not a coprime of %d!' % alpha_len)
        else:
            for ch in message:
                if ch in self.alpha:
                    letter_pos = (self.alpha).find(ch)
                    letter = self.alpha[(letter_pos - key_2) * inv_a % alpha_len]
                    self.plaintext += letter
                else:
                    self.plaintext += ch
        return self.plaintext
    
    def gen_coprime(self):
        """
            :return list of valid numbers for key_1. If key_1 does not exist
            in coprime, we raise a ValueError.
        """
        coprime = [num for num in range(len(self.alpha)) if num % 2 != 0]
        return coprime

"""
# Test Cases:

message = "Affine3 Ciphe4r"
Test = Affine(message=message, key_1=5, key_2=8, encrypt=True)
print('Encrypted Message : %s' % Test)
dec_message = "oHHWlCJ yWvRCOF"
Test2 = Affine(message=dec_message, key_1=5, key_2=8, encrypt=False)
print('Decrypted Message : %s' % Test2)

atbashmessage = 'Atbash Cipher'
Test3 = Affine(message=atbashmessage, atbash=True)
print('Encode Atbash : %s' % Test3)
Test4 = Affine(message="zGYZHS xRKSVI", atbash=True)
print('Decode Atbash : %s' % Test4)

"""
