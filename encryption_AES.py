
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#key generation ingredients
salt = get_random_bytes(16)
password = "Heisenberg"

# an algorithm that generates key such it cannot be broken by brute-force
key = PBKDF2(password, salt, dkLen=32)
key_file = open("key.bin","wb")
key_file.write(key)
key_file.close()

# loading the file to be encrypted
original_file = open("details.txt","r")
message = original_file.read()
cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(bytes(message, 'utf-8'), AES.block_size))
#encrypting and storing in an external file
with open('encrypted.nomem','wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
