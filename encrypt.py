from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from os.path import isfile

archivo = 'mensaje.txt'

#se llama al archivo de texto para cifrar
if isfile(archivo):

    with open(archivo, 'r') as file:
        data = file.read().replace('\n', '-')

else:
    print("Archivo inexistente")

#se convierte en bytes el string generado del archivo que necesitamos cifrar su contenido
mcryt = bytes(data, encoding='utf8')


try:
    #se llama a la llave publica generada para cifrar el mensaje
    with open("publ.pem", "rb") as f:
        public_key = f.read()
        public_key = RSA.importKey(public_key)
    RSA_encryptor = PKCS1_OAEP.new(public_key)
    encrypted_mens = RSA_encryptor.encrypt(mcryt)
except IOError:
    print("Error el ejecutar")
except:
    encrypted_mens = None

#aqui mostramos el mensaje cifrado
print(encrypted_mens)

#se genera un archivo con el mensaje cifrado
with open("mensaje.bin", "wb") as f:
    f.write(encrypted_mens)