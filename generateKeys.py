from Cryptodome.PublicKey import RSA

key = RSA.generate(2048)

with open("priv.pem", "wb") as f:
    f.write(key.export_key('PEM'))

with open("publ.pem", "wb") as f:
    f.write(key.public_key().export_key('PEM'))

