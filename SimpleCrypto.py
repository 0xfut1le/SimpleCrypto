import logging
import argparse
import os
import sys

from Affine import Affine
from Caesar import CaesarCipher
from ColumnTransposition import ColTransposition
from Encodings import Encodings
from KeywordCipher import KeywordCipher
from Railfence import Railfence

# Update valid_ciphers for any added ciphers
valid_ciphers = ['AtBash', 'Affine', 'Caesar', 'ColTransposition', 
                    'Keyword', 'Railfence', 'Base16', 'Base32', 'Base64', 
                    'Base85']

parser = argparse.ArgumentParser(
    prog='SimpleCrypto', 
    description="SimpleCrypto - encrypt, decrypt messages using a collection of simple cryptographic ciphers and encodings.",
    epilog="Written by 0xByte"
)
parser.add_argument('-e', action='store', 
    choices=valid_ciphers,
    dest='cipher_type',
    required=True,
    help='Cipher / Encoding to process message with.'
)
parser.add_argument('--key', dest='key',
    nargs='+',
    default=None,
    type=int,
    help='Used to encrypt / decrypt messages'
)
parser.add_argument('--keyword', dest='keyword',
    nargs=1,
    default=None,
    type=str,
    help='Used in special cases to encrypt / decrypt messages'
)

# Set mode to Encrypt or Decrypt message
mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument('--encrypt', action='store_true', dest='encrypt')
mode.add_argument('--decrypt', action='store_false', dest='encrypt')

# Require message from CLI or File input
message_input = parser.add_mutually_exclusive_group(required=True)
message_input.add_argument('-m', '--message', action='store', 
    help='Load message from CLI',
    dest='message'
)
message_input.add_argument('-f', '--file', 
    action='store', help='Load message from file. Takes file path as argument.',
    dest='message_file'
)

def load_from_file(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError
    with open(file=filepath, mode="r") as file:
        message = file.read().replace("\n", " ")
    return message

def main():
    args = parser.parse_args()
    
    cipher_type = args.cipher_type
    key = args.key
    keyword = None
    message = args.message
    message_file = args.message_file
    mode = args.encrypt
    
    # If message is None, we can assume we need to load message from file
    if not message:
        message = load_from_file(message_file)
    
    # Make sure args.keyword exists before local assignment
    if not args.keyword:
        keyword = None
    else:
        keyword = args.keyword[0]
    
    # Custom Result message
    if mode:
        cipher_prefix = '[+] Ciphertext: '
    else:
        cipher_prefix = '[+] Plaintext: '

    # Define what to do with the arguments
    if cipher_type == 'AtBash':
        print(cipher_prefix + str(Affine(message=message, atbash=True)))
    elif cipher_type == 'Affine':
        if len(key) != 2:
            parser.error('Affine ciphers require two key values. Delimit each key with a space.')
        print(cipher_prefix + str(Affine(message=message, key_1=key[0], key_2=key[1], encrypt=mode)))
    elif cipher_type == 'Caesar':
        if mode:
            print(cipher_prefix + str(CaesarCipher(message=message, offset=key[0], encode=mode).encoded))
        else:
            print(cipher_prefix + str(CaesarCipher(message=message, offset=key[0], encode=mode).decoded))
    elif cipher_type == 'ColTransposition':
        if not keyword:
            parser.error('Missing --keyword argument/value!')
        print(cipher_prefix + str(ColTransposition(message=message, keyword=keyword, encrypt=mode)))
    elif cipher_type == 'Keyword':
        if not keyword:
            parser.error('Missing --keyword argument/value')
        print(cipher_prefix + str(KeywordCipher(message=message, keyword=keyword, encrypt=mode)))
    elif cipher_type == 'Railfence':
        if not key:
            parser.error('Missing --key argument/value')
        print(cipher_prefix + str(Railfence(message=message, key=key[0], encrypt=mode)))
    elif cipher_type == 'Base16' or cipher_type == 'Base32' or cipher_type == 'Base64' or cipher_type == 'Base85':
        print(cipher_prefix + str(Encodings(string=message, encoding=cipher_type, encode=mode)))


if __name__ == "__main__":
    main()
