# SimpleCrypto   
Requirements: Python 3.8+   

A Simple Python library to compute basic ciphers and encodings from the command line.   
This is an ongoing project that is being built solely for the experience.

```
usage: SimpleCrypto [-h] -e {AtBash,Affine,Caesar,ColTransposition,Keyword,Railfence,Base16,Base32,Base64,Base85} [--key KEY [KEY ...]] [--keyword KEYWORD]
                    (--encrypt | --decrypt) (-m MESSAGE | -f MESSAGE_FILE)

SimpleCrypto - encrypt, decrypt messages using a collection of simple cryptographic ciphers and encodings.

optional arguments:
  -h, --help            show this help message and exit
  -e {AtBash,Affine,Caesar,ColTransposition,Keyword,Railfence,Base16,Base32,Base64,Base85}
                        Cipher / Encoding to process message with.
  --key KEY [KEY ...]   Used to encrypt / decrypt messages
  --keyword KEYWORD     Used in special cases to encrypt / decrypt messages
  --encrypt
  --decrypt
  -m MESSAGE, --message MESSAGE
                        Load message from CLI
  -f MESSAGE_FILE, --file MESSAGE_FILE
                        Load message from file. Takes file path as argument.
```
