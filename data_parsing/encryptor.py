from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from cryptography import fernet
from Crypto import Hash
from Crypto import Random
import argparse
import logging
import hashlib
import base64
import uuid
import time

class Encryptor:

    def __init__(self, path=''):
        if path == '':
            print('No key import executed')
        self.arg_parser = argparse.ArgumentParser()
        self.arg_parser.add_argument(
            '-v', '--verbose',
            help='Increase output verbosity',
            action="store_true")
        self.args = self.arg_parser.parse_args()

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
        if self.args.verbose == True:
            print("==> Generating new keypair...")
        keysize = 256*4
        private_key = RSA.generate(keysize, Random.new().read)
        public_key = private_key.publickey()
        return private_key, public_key

    def encrypt(self, data, public_key, encode=False):
        if self.args.verbose == True:
            print(f"==> Encrypting: {data}")
        encryptor = PKCS1_OAEP.new(public_key)
        if encode: encrypted_data = encryptor.encrypt(data.encode())
        else: encrypted_data = encryptor.encrypt(data)
        return encrypted_data

    def decrypt(self, encrypted_data, private_key, decode=True):
        if self.args.verbose == True:
            print(f"==> Decrypting: {encrypted_data}")
        decryptor = PKCS1_OAEP.new(private_key)
        decrypted_data = decryptor.decrypt(encrypted_data)
        if decode == True: return decrypted_data.decode()
        else: return decrypted_data


