import os
import pyaes

## abrir o arquivo criptografado
file_name = "credenciais.txt.ransomware"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"qwertyuiop123456"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)



## criar o arquivo descriptografado
new_file = "credenciais.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()

## remover o arquivo criptografado
os.remove(file_name)