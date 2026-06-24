# Repetindo 5 vezes
for numero in range(5):
    print("Executando...")

# Mostrando os números
print(list(range(5)))

for numero in range(5):
    print(numero)

# Começando de outro número
for numero in range(1, 6):
    print(numero)

# Definindo passos
for numero in range(0, 10, 2):
    print(numero)

# Contador simples
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# Exemplo prático para QAs
tentativas = 0

while tentativas < 3:
    print("Tentando login...")
    tentativas += 1

# Interrompendo e controlando loops
contador = 0

while contador < 10:
    print(contador)

    if contador == 5:
        break

    contador += 1

for numero in range(10):
    if numero == 3:
        break
    print(numero)

for numero in range(6):
    if numero == 3:
        continue
    print(numero)

contador = 0

while contador < 6:
    contador += 1

    if contador == 3:
        continue

    print(contador)

# Exemplo prático para QAs
status_codes = [200, 200, 500, 200]

for status in status_codes:
    if status == 500:
        print(f"Status: {status}, erro encontrado.")
        break
    else:
        print(f"Status: {status}")

status_codes = [200, 200, 500, 200]

for status in status_codes:
    if status == 200:
        continue

    print("Status diferente de 200:", status)
