from base import Cipher
import string

class KeywordCipher(Cipher):
    def __init__(self, message=None, keyword=None, encrypt=False):
        """
            This cipher is very similar to how the Caesar cipher works
            instead of using keys to shift the message, we take in a
            keyword that shifts the standard alpha over and removes any
            duplicate values after the first occurence of a letter.

            Next, for each letter in the message, the letter is replaced
            by the equivalent letter in the generated alpha.

            Example:
            :keyword keyword
            produces custom_alpha = KEYWORDABCFGHIJLMNPQSTUVXZ
            alpha_key = [(A, K), (B, E), (C, Y)...]
            :keyword CyberGym
            produces custom_alpha = CYBERGMADFHIJKLNOPQSTUVWXZ
            alpha_key = [(A, C), (B, Y), (C, B), ...]
        """
        self.message    = message
        self.keyword    = keyword
        self.encrypt    = encrypt
        self.plaintext  = ''
        self.ciphertext = ''
    
    def __repr__(self):
        if self.encrypt:
            return self.enc_keyword_cipher()
        else:
            return self.dec_keyword_cipher()

    def enc_keyword_cipher(self):
        """
            :param  keyword: used to create custom alphabet
            :return: ciphertext of message encrypted with custom alphabet

            This function loops through the plaintext and replaces each
            letter with the corresponding letter in the standard alphabet. 
        """
        alpha_key = self.gen_keyword_alpha()
        message = self.message.upper()

        for letter in message:
            if letter == " " or letter == '{' or letter == '}':
                self.ciphertext += letter
            else:
                for item in alpha_key:  
                    if letter in item[0]:
                        self.ciphertext += item[1]
        return self.ciphertext


    def dec_keyword_cipher(self):
        """
            :param  keyword: used to create custom alphabet
            :return: plaintext of message encrypted with custom alphabet

            This function loops through the ciphertext and replaces each
            letter with the corresponding letter in the standard alphabet. 
        """        
        alpha_key = self.gen_keyword_alpha()
        message = self.message.upper()
        #   Search for letter from message in alpha_key[1] and append the corresponding 
        #   standard_alpha value to get plaintext.
        for letter in message:
            if letter == " " or letter == '{' or letter == '}':
                self.plaintext += letter
            else:
                for item in alpha_key:
                    if letter in item[1]:
                        self.plaintext += item[0]
        return self.plaintext


    def gen_keyword_alpha(self):
        """
            :return List of tuples containing the keyword alpha paired with
            the associated standard alpha value.

            We use a keyword to make a custom alphabet where the keyword 
            shifts all letters over. Any duplicates following the first 
            occurrence of a letter are removed.

            Example:
            :keyword keyword
            produces custom_alpha = KEYWORDABCFGHIJLMNPQSTUVXZ
            alpha_key = [(A, K), (B, E), (C, Y)...]
            :keyword CyberGym
            produces custom_alpha = CYBERGMADFHIJKLNOPQSTUVWXZ
            alpha_key = [(A, C), (B, Y), (C, B), ...]

        """
        keyword = ''
        standard_alpha = string.ascii_uppercase

        # First remove any duplicate value from keyword
        for ch in self.keyword.upper():
            if ch not in keyword:
                keyword += ch
        # Remove duplicate values and append keyword and standard_alpha to create custom_alpha
        custom_alpha = keyword
        for ch in standard_alpha:
            if ch not in keyword:
                custom_alpha += ch
        # Pack the two alphabets into a list of tuples for easy access later
        alpha_key = list(zip(standard_alpha, custom_alpha))
        return alpha_key
