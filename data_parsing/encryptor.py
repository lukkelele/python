from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from cryptography import fernet
from Crypto import Hash
from Crypto import Random
import argparse
import logging
import hashlib
import uuid
import base64

class Encryptor:

    def __init__(self, path=''):
        if path == '':
            print('No key import executed')

    def hash(self, password, salt):
        return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ":" + salt

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        hashed_password = hash(password, salt)
        return hashed_password

    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(":")
        hashed_user_password = hash(user_password, salt)
        if hashed_user_password == password: return True
        else: return False

    def SHA512_hash(self, data):
        SHA_hash = Hash.SHA512.new(data.encode("utf8"))
        encrypted_data = SHA_hash.digest()
        return encrypted_data

    def generate_keypair(self):
        keysize = 256*4
        private_key = RSA.generate(keysize, Random.new().read)
        public_key = private_key.publickey()
        return private_key, public_key

    def encrypt(self, data, public_key, verbose=False):
        encryptor = PKCS1_OAEP.new(public_key)
        encrypted_data = encryptor.encrypt(data.encode())
        return encrypted_data

    def decrypt(self, encrypted_data, private_key, decode=True, verbose=False):
        decryptor = PKCS1_OAEP.new(private_key)
        decrypted_data = decryptor.decrypt(encrypted_data)
        if decode == True: return decrypted_data.decode()
        else: return decrypted_data

test = 'lukas'
e = Encryptor()
private_key, public_key = e.generate_keypair()
encrypted_msg = e.encrypt(test, public_key)
decrypted_msg = e.decrypt(encrypted_msg, private_key)
print(encrypted_msg)
print(decrypted_msg)

