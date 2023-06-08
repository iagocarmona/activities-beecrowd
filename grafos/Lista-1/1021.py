# 1021 - Notas e Moedas
dinheiro = float(input())

notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

result_notas = [0, 0, 0, 0, 0, 0]
result_moedas = [0, 0, 0, 0, 0, 0]

for i in range(len(notas)):
    while dinheiro >= notas[i]:
        dinheiro -= notas[i]
        result_notas[i] += 1

for i in range(len(moedas)):
    while dinheiro >= moedas[i]:
        dinheiro -= moedas[i]
        dinheiro = round(dinheiro, 2)
        result_moedas[i] += 1
        
print("NOTAS:")
for i in range(len(notas)):
    if result_notas[i] > 0:
        print(f"{result_notas[i]} nota(s) de R$ {notas[i]:.2f}")
    else:
        print(f"0 nota(s) de R$ {notas[i]:.2f}")

print("MOEDAS:")
for i in range(len(moedas)):
    if result_moedas[i] > 0:
        print(f"{result_moedas[i]} moeda(s) de R$ {moedas[i]:.2f}")
    else:
        print(f"0 moeda(s) de R$ {moedas[i]:.2f}")