valores = input().split()

# 12 KM/L
tempo = int(valores[0])
velocidade = int(valores[-1])

distancia = velocidade * tempo;

combistivel_gasto = distancia / 12

print(f"{combistivel_gasto:.3f}")

