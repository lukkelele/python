from cryptography import fernet
from Crypto import Random
from Crypto import Hash 
import hashlib
import uuid


def hash(password, salt):
    return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ":" + salt

def hash_password(password):
    salt = uuid.uuid4().hex
    hashed_password = hash(password, salt)
    return hashed_password

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(":")
    hashed_user_password = hash(user_password, salt)
    if hashed_user_password == password: return True
    else: return False

def SHA512_hash(data):
    SHA_hash = Hash.SHA512.new(data.encode("utf8"))
    encrypted_data = SHA_hash.digest()
    return encrypted_data

def generate_keypair(KEYSIZE):
    keys = []
    for i in range(2):
        keys.append(Random.get_random_bytes(KEYSIZE))
    private_key, public_key = keys[0], keys[1]
    return private_key, public_key


test_data = 'Lukas'

