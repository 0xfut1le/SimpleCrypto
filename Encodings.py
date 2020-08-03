from base import Cipher
import base64

class Encodings(Cipher):
    def __init__(self, string=None, encoding=None, encode=False):
        self.string = string
        self.encoding = encoding
        self.encode = encode
        self.message = ""

    def __repr__(self):
        if self.encoding == 'Base64':
            return self.base64_encoding()
        elif self.encoding == 'Base32':
            return self.base32_encoding()
        elif self.encoding == 'Base16':
            return self.base16_encoding()
        elif self.encoding == 'Base85':
            return self.base85_encoding()
        
    def base64_encoding(self):
        if not self.encode:
            try:
                self.message = str(base64.b64decode(self.string).decode('UTF-8'))
            except ValueError:
                return "Invalid Chars: String is not a Base64 Decodable String..."
            return self.message
        else:
            self.message = str(base64.b64encode(self.string.encode('UTF-8')))
            return self.message
    
    def base32_encoding(self):
        if not self.encode:
            try:
                self.message = str(base64.b32decode(self.string).decode('UTF-8'))
            except ValueError:
                return "Invalid Chars: String is not a Base32 Decodable String..."
            return self.message
        else:
            self.message = str(base64.b32encode(self.string.encode('UTF-8')))
            print(self.message)
            return self.message
    
    def base16_encoding(self):
        if not self.encode:
            try:
                self.message = str(base64.b16decode(self.string).decode('UTF-8'))
            except ValueError:
                return "Invalid Chars: String is not a Base16 Decodable String..."
            return self.message
        else:
            self.message = str(base64.b16encode(self.string.encode('UTF-8')))
            return self.message
    
    def base85_encoding(self):
        if not self.encode:
            try:
                self.message = str(base64.b85decode(self.string).decode('UTF-8'))
            except ValueError:
                return "Invalid Chars: String is not a Base85 Decodable String..."
            return self.message
        else:
            self.message = str(base64.b85encode(self.string.encode('UTF-8')))
            return self.message
