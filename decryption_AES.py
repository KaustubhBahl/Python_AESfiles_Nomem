from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#loading the key for decryption
f = open("key.bin","rb")
key = f.read()

#loading the encrypted file
with open('encrypted.nomem','rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

#creating decrypted file
with open('decrypted.txt','w') as f1 :
    f1.write(original.decode('utf-8'))
