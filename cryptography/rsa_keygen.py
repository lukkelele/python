from Crypto.PublicKey import RSA
from os import urandom, read
import base64

mod = 256

# Generate a key with a length of 256*n bits
def generate_keys(n):
    key = RSA.generate(mod*n)
    privkey, pubkey = key.export_key(), key.publickey().export_key()
    return privkey, pubkey

# Save the keys encoded in b64
def save_keys(privkey, pubkey, path="./"):
    for i in range(2):
        if i == 0:
            key = encode_b64(privkey)
            keyname = 'private.pem'
        else:
            key = encode_b64(pubkey)
            keyname = 'public.pem'
        file = open(keyname, 'wb')
        file.write(key)

def encode_b64(obj):
    return base64.b64encode(obj)

def decode_b64(obj):
    return base64.b64decode(obj)

def load_keys(path="./", ext="pem"):
    privkey = open(f"{path}private.{ext}", 'r').read()
    pubkey = open(f"{path}public.{ext}", 'r').read()
    decoded_privkey = decode_b64(privkey).decode()
    decoded_pubkey = decode_b64(pubkey).decode()
    return decoded_privkey, decoded_pubkey



