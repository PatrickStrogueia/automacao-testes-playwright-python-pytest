ambientes = ["desenvolvimento", "homologação", "produção"]

print(ambientes[0])
print(ambientes[1])
print(ambientes[2])

# exibição da lista em ordem inversa
print(ambientes[-1])
print(ambientes[-2])
print(ambientes[-3])

# exemplos para QAs

execucoes = ["PASSOU", "PASSOU", "FALHOU", "PASSOU"]

ultimo_resultado = execucoes[-1]
print(f"Resultado mais recente: {ultimo_resultado}")

# modificando valores

usuarios = ["ana@email.com", "carlos@email.com", "maria@email.com"]

usuarios[1] = "carlos@email.com"

print(usuarios)

# adicionando elementos

# append() adicionar no final

usuarios = ["ana@email.com", "carlos@email.com"]

usuarios.append("maria@email.com")
usuarios.append("pedro@email.com")

print(usuarios)

# insert() adicionar em posição específica

usuarios = ["ana@email.com", "carlos@email.com"]

usuarios.insert(0, "admin@email.com")

print(usuarios)

# 7. removendo elementos

# remove() remover pelo valor

usuarios = ["ana@email.com", "carlos@email.com", "maria@email.com"]

usuarios.remove("carlos@email.com")

print(usuarios)

# pop() remover pelo índice

usuarios = ["ana@email.com", "carlos@email.com", "maria@email.com"]

removido = usuarios.pop(1)

print(f"Usuário removido: {removido}")
print(f"Lista atualizada: {usuarios}")

# 8. descobrindo o tamanho da lista

# len() informa quantos elementos existem na lista

resultados_api = ["item1", "item2", "item3", "item4", "item5"]

total = len(resultados_api)

print(f"Total de resultados: {total}")

esperado = 5

#if(len(resultados_api) == esperado):
if(total == esperado):
    print("Quantidade de resultados correta!")
else:
    print(f"Esperava {esperado}, mas veio {len(resultados_api)}.")

# 9. percorrendo listas com loops

# loop simples com for

ambientes = ["desenvolvimento", "homologação", "produção"]

for ambiente in ambientes:
    print(f"Testando em: {ambiente}")

# loop com índice usando enumarate()

casos_de_teste = ["Login válido", "Login inválido", "Login sem senha"]

print(enumerate(casos_de_teste))
print(list(enumerate(casos_de_teste)))

for indice, valor in enumerate(casos_de_teste):
    print(f"Caso {indice + 1}: {valor}")

# 10. verificando se um item existe

# use o operador in para checar se um valor está presente na lista

codigos_sucesso = [200, 201, 204]

codigo_recebido = 201

if codigo_recebido in codigos_sucesso:
    print(f"Código {codigo_recebido} é um código de sucesso.")
else:
    print(f"Código {codigo_recebido} não era esperado.")

# você também pode utilizar not in para verificar a ausência

erros_criticos = [500, 502, 503]

codigo = 404

if codigo not in erros_criticos:
    print(f"Código {codigo} não é um erro crítico do servidor.")
