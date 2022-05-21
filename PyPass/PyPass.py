from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import sys

"""
Ruben Hinojar ----------- Python Encryption ----------- 06/12/2021
"""

"""
Prepare a USB flash drive with the letter Z:/ and insert the files 'privkey.pem' and 'pubkey.pem' that 
come with this program. It is necessary to delete the contents of these two files

You have to create a file named 'secret.txt' in the same directory as this '.py' file
Before executing this program, the file 'secret.txt' must be filled with the word we want to hide.
We proceed to encrypt and decrypt the word to see the result
"""

file_priv = open('Z:/privkey.pem', 'r')
privkey = file_priv.read()
file_priv.close()
file_pub = open('Z:/pubkey.pem', 'r')
pubkey = file_pub.read()
file_pub.close()

#In case the files are empty, the keys are generated again.
if privkey == '' or pubkey == '':
    def export_private_key(privkey, filename):
        file_priv = open(filename, 'wb')
        file_priv.write(privkey.exportKey('PEM', passphrase=None))
        file_priv.close()

    def export_public_key(pubkey, filename):
        file_pub = open(filename, 'wb')
        file_pub.write(pubkey.exportKey('PEM', passphrase=None))
        file_pub.close()

    privkey = RSA.generate(2048)
    pubkey = privkey.publickey()

    export_private_key(privkey, 'Z:/privkey.pem')
    export_public_key(pubkey, 'Z:/pubkey.pem')

#If we have found keys, we import them
else:
    def import_private_key(filename):
        file_priv = open(filename, 'rb')
        privkey = RSA.importKey(file_priv.read(), passphrase=None)
        file_priv.close()
        return privkey

    def import_public_key(filename):
        file_pub = open(filename, 'rb')
        pubkey = RSA.importKey(file_pub.read(), passphrase=None)
        file_pub.close()
        return pubkey

    privkey = import_private_key('Z:/privkey.pem')
    pubkey = import_public_key('Z:/pubkey.pem')

encrypt_process = int(input('0 for decrypt and 1 for encrypt: '))

#We encrypt the word we have in the file 'secret.txt' when we enter the value 1.
if encrypt_process == 1:
    secret_file = open('secret.txt', 'r')
    secret = secret_file.read()
    secret_file.close()

    rsa_cipher = PKCS1_OAEP.new(pubkey)
    encrypted = rsa_cipher.encrypt(secret.encode())

    secret_file = open('secret.txt', 'wb')
    secret_file.write(encrypted)
    secret_file.close()
    print('\n' + str(encrypted))

#In case we enter the value 0, we decode the hidden word in the file 'secret.txt'.
else:
    secret_file = open('secret.txt', 'rb')
    encrypted = secret_file.read()
    secret_file.close()

    rsa_cipher = PKCS1_OAEP.new(privkey)
    decrypted = rsa_cipher.decrypt(encrypted)
    lista = list(decrypted)

    decrypted = bytes(lista)
    print('\nDecoded message: ' + decrypted.decode())