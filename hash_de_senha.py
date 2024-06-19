import hashlib

senha = input("Digite a senha: ")
senha_em_bytes = senha.encode()

objeto_hash = hashlib.sha256(senha_em_bytes)
hash_hexadecimal = objeto_hash.hexdigest()

print("O hash da senha é:", hash_hexadecimal)