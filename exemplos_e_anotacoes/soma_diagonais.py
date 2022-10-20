import math

arr = [ [1, 2, 3], [4, 5, 6], [9, 8, 9] ]

diagonal_1 = 0
diagonal_2 = 0
tamanho_matrix = range(int(math.sqrt(len(arr))))

for i in arr:
    for j in arr:
        if i == j:
            print (j)

print (diagonal_1)