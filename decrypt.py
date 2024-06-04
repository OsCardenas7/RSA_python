from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

try:
    #se llama la llave privada para su uso
    with open("priv.pem", "rb") as f:
        priv_key = f.read()
        priv_key = RSA.importKey(priv_key)
    RSA_encryptor = PKCS1_OAEP.new(priv_key)

    #se hace llamado del archivo que contiene los datos cifrados el mensaje
    with open("mensaje.bin", "rb") as f:
        mens = f.read()
    
    #se decifra el mensaje
    texto = RSA_encryptor.decrypt(mens)
except IOError:
    print("ERROR AL DESCENCRIPTAR")
except:
    texto = None

#se muestra el mensaje decifrado en pantalla
print(str(texto, encoding='utf8'))