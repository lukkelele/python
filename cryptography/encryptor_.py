from cryptography.fernet import Fernet
from Crypto import Hash
from Crypto import Random
import hashlib
import base64
import uuid
import time

class Encryptor:

    def __init__(self, key_dir=''):
        if key_dir == '': 
            self.generate_key()
            self.key = self.load_key("./")
        else: self.key = self.load_key(key_dir) 

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

    def generate_key(self, key_dir=''):
        key = Fernet.generate_key()
        if key_dir == '':
            with open("enckey.key", "wb") as key_file:
                key_file.write(key)
        else:
            key_path = key_dir + 'enckey.key'
            with open(key_path, "wb") as key_file:
                key_file.write(key)

    def load_key(self, key_dir):
        key_dir += 'enckey.key'
        return open(key_dir, "rb").read()

    def encrypt(self, data, key):
        enc = Fernet(key)
        encrypted_data = enc.encrypt(data.encode())
        return encrypted_data

    def decrypt(self, data, key):
        enc = Fernet(key)
        decrypted_data = enc.decrypt(data)
        return decrypted_data.decode()
