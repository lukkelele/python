from cryptography import fernet
from Crypto.PublicKey import RSA
from Crypto import Hash
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import hashlib
import uuid
import base64


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

def generate_keypair():
    keysize = 256*4
    private_key = RSA.generate(keysize, Random.new().read)
    public_key = private_key.publickey()
    return private_key, public_key

def encrypt(data, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted_data = encryptor.encrypt(data.encode())
    return encrypted_data

def decrypt(encrypted_data, private_key, decode=True):
    decryptor = PKCS1_OAEP.new(private_key)
    decrypted_data = decryptor.decrypt(encrypted_data)
    if decode == True: return decrypted_data.decode()
    else: return decrypted_data

test_data = 'Lukas'
priv_key, pub_key = generate_keypair()
print(f"Encrypted data: {encrypt(test_data, pub_key)}")
encrypted_data = encrypt(test_data, pub_key)
print(f"Decrypted data: {decrypt(encrypted_data, priv_key)}")
