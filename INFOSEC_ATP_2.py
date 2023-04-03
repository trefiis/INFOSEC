import hashlib
hash_256 = input('Coloque o valor de Hash 256:\n')
hash_md5 = input('Coloque o valor de Hash MD5:\n')
frase = input('Cole a frase:\n')

frase_string_sha256 = hashlib.sha256(frase.encode('utf-8')).hexdigest()
frase_string_md5 = hashlib.md5(frase.encode('utf-8')).hexdigest()

print(frase_string_sha256)
print(frase_string_md5)
print(frase_string_sha256 == hash_256)
print(frase_string_md5 == hash_md5)

