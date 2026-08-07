usuario = {
    "nome": "Patrick",
    "idade": 33,
    "ativo": True
}

print(usuario)
print(usuario.keys())
print(usuario.values())

# 3. acessando valores

print(usuario["nome"])
print(usuario["idade"])
print(usuario["ativo"])

# 4. adicionando novos valores

usuario["cidade"] = "Campo Grande"
print(usuario)

# 5. alterando valores

usuario["ativo"] = False

print(usuario)

# 6. removendo valores

item_removido = usuario.pop("cidade")
print(item_removido)
print(usuario)

# 7. descobrindo o tamanho

print(len(usuario))

# 8. percorrendo dicionários

for valor in usuario:
    print(valor)

print(usuario.items())

for chave, valor in usuario.items():
    print(chave, valor)

for chave in usuario.keys():
    print(chave)

# 10. verificando se uma chave exite

if "nome" in usuario:
    print("Chave encontrada")

if "nome" in usuario.keys():
    print("Chave encontrada")

if "Patrick" in usuario:
    print("Valor encontrado")
else:
    print("Valor não encontrado")

if "Patrick" in usuario.keys():
    print("Valor encontrado")

print(usuario.keys())
print(usuario.items())
print(usuario.values())

# 11. aplicação prática para QA

resposta_api = {
    "status_code": 200,
    "mensagem": "Sucesso",
    "tempo_resposta": 120
}

if resposta_api["status_code"] != 200:
    print("Erro na API")

print("Tempo de resposta: ", resposta_api["tempo_resposta"])
