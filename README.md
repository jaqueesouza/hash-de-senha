# hash-de-senha
Um programa simples para criptografar senhas dos usuários com Python.


## Explicando 

1. Para este programa eu usei da biblioteca hashlib. Ela é uma biblioteca nativa do python para gerar hashes de dados, então comecei importando ela com o comando "import hashlib"
2. Na segunda parte é onde pedimos a senha do usuário, com um comando simples de input: senha = input("Digite a senha: ")
3. Depois é preciso transformar essa str em bytes, já que a biblioteca trabalha dessa forma, com isso usamos o comando: senha_em_bytes = senha.encode()
4. Para a proxima parte usei o algoritmo SHA-256 para gerar o hash da senha. Para isso, criamos um objeto hash usando "hashlib.sha256()" e passamos a senha em bytes como argumento: objeto_hash = hashlib.sha256(senha_em_bytes)
5. Em seguida vamos obter o hash em formato hexadecimal (uma sequência de letras e números), que é uma das formas mais comum de representar hashes: hash_hexadecimal = objeto_hash.hexdigest()
6. Por fim, precisamos exibir esse hash para o usuário (importante kk). Geramos ele dessa forma: print("O hash da senha é:", hash_hexadecimal)

## Como Usar

1. **Instalação:** É preciso ter o Python instalado no seu sistema.
2. **Execução:** Abra o terminal, navegue até a pasta do projeto e digite `python hash_de_senha.py`.
3. **Digite a senha:** Quando solicitado, digite a senha que você deseja gerar o hash.
4. **Visualize o hash:** O hash gerado será exibido no terminal.

## Funcionalidades

* Gera hashes de senhas usando o algoritmo SHA-256.
* Converte a senha para bytes antes de gerar o hash.
* Exibe o hash gerado em formato hexadecimal.
