# EXERCICIOS MATRIZES - FINAL

# Ex 1 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# print(np.sum(matriz))

#---------------------------------------------------
# Ex 2 ->
# import numpy as np
#
# n = int(input("Digite n: "))
# identidade = np.eye(n)
#
# print(identidade)

#---------------------------------------------------
# Ex 3 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]])
#
# num = int(input("Digite um número: "))
#
# print(num in matriz)

#---------------------------------------------------
# Ex 4 ->
# import numpy as np
#
# matriz = np.array([[1, 2],
#                    [3, 4]])
#
# matriz[[0, 1]] = matriz[[1, 0]]
#
# print(matriz)

#---------------------------------------------------
# Ex 5 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# escalar = float(input("Digite um número: "))
#
# print(matriz * escalar)

#---------------------------------------------------
# Ex 6 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12]])
#
# pares = np.sum(matriz % 2 == 0)
#
# print(pares)

#---------------------------------------------------
# Ex 7 ->
# import numpy as np
#
# matriz = np.random.randint(1, 100, (3, 3))
#
# print(matriz)
# print(np.max(matriz))

#---------------------------------------------------
# Ex 8 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# print(np.mean(matriz, axis=1))

#---------------------------------------------------
# Ex 9 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]])
#
# print(np.trace(matriz))

#---------------------------------------------------
# Ex 10 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3],
#                    [4, 5, 6]])
#
# print(matriz.T)

#---------------------------------------------------
# Ex 11 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# print(np.sum(matriz, axis=0))

#---------------------------------------------------
# Ex 12 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3],
#                    [2, 5, 6],
#                    [3, 6, 9]])
#
# print(np.array_equal(matriz, matriz.T))

#---------------------------------------------------
# Ex 13 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3, 4, 5],
#                    [6, 7, 8, 9, 10],
#                    [11, 12, 13, 14, 15],
#                    [16, 17, 18, 19, 20],
#                    [21, 22, 23, 24, 25]])
#
# n = len(matriz)
# for i in range(n):
#     print(matriz[i][n - i - 1])

#---------------------------------------------------
# Ex 14 ->
# import numpy as np
#
# A = np.array([[1, 2],
#               [3, 4]])
#
# B = np.array([[5, 6],
#               [7, 8]])
#
# print(np.dot(A, B))

#---------------------------------------------------
# Ex 15 ->
# def rotacionar(matriz):
#     n = len(matriz)
#     nova = [[0]*n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             nova[j][n-1-i] = matriz[i][j]
#
#     return nova
#
# matriz = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(rotacionar(matriz))