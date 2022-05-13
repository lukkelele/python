from cryptography.fernet import Fernet
from Crypto import Hash
from Crypto import Random
import argparse
import logging
import hashlib
import base64
import uuid
import time

class Encryptor:

    def __init__(self, key_path=''):
        if key_path == '': 
            self.generate_key()
            self.key = self.load_key()
        else: self.key = self.load_key() 

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

    def generate_key(self):
        key = Fernet.generate_key()
        with open("enckey.key", "wb") as key_file:
            key_file.write(key)
        return key      # TODO: Remove this later

    def load_key(self, key_dir):
        key_dir += '/enckey'
        return open(key_dir, "rb").read()

    def encrypt(self, data, key):
        enc = Fernet(key)
        encrypted_data = enc.encrypt(data.encode())
        print(encrypted_data)
        return encrypted_data

    def decrypt(self, data, key):
        enc = Fernet(key)
        decrypted_data = enc.decrypt(data)
        print(decrypted_data.decode())
        return decrypted_data.decode()
