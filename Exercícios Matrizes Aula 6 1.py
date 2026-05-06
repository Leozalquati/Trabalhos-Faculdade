# EXERCICIOS MATRIZES - NUMPY

# Ex 1 ->
# import numpy as np
#
# manha = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# tarde = np.array([[1, 1, 1],
#                    [2, 2, 2],
#                    [3, 3, 3]])
#
# total = manha + tarde
#
# print("Matriz manhã:")
# print(manha)
#
# print("Matriz tarde:")
# print(tarde)
#
# print("Matriz total:")
# print(total)

#---------------------------------------------------
# Ex 2 ->
# import numpy as np
#
# estoque_inicial = np.array([[10, 20, 30],
#                              [40, 50, 60],
#                              [70, 80, 90]])
#
# vendidos = np.array([[1, 2, 3],
#                       [4, 5, 6],
#                       [7, 8, 9]])
#
# estoque_final = estoque_inicial - vendidos
#
# print("Estoque inicial:")
# print(estoque_inicial)
#
# print("Vendidos:")
# print(vendidos)
#
# print("Estoque final:")
# print(estoque_final)

#---------------------------------------------------
# Ex 3 ->
# import numpy as np
#
# ingredientes = np.array([[1, 2, 3],
#                           [4, 5, 6]])
#
# pedidos = np.array([[1, 2],
#                      [3, 4],
#                      [5, 6]])
#
# resultado = np.dot(ingredientes, pedidos)
#
# print("Ingredientes:")
# print(ingredientes)
#
# print("Pedidos:")
# print(pedidos)
#
# print("Resultado:")
# print(resultado)

#---------------------------------------------------
# Ex 4 ->
# import numpy as np
#
# salarios = np.array([[1000, 1500, 2000],
#                      [2500, 3000, 3500],
#                      [4000, 4500, 5000]])
#
# reajustado = salarios * 1.10
#
# print("Salários originais:")
# print(salarios)
#
# print("Salários reajustados:")
# print(reajustado)

#---------------------------------------------------
# Ex 5 ->
# import numpy as np
#
# matriz = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# matriz[:] = 0
#
# print("Matriz zerada:")
# print(matriz)

#---------------------------------------------------
# Ex 6 ->
# import numpy as np
#
# matriz = np.array([[2, 3, 4, 5],
#                    [6, 7, 8, 9],
#                    [1, 2, 3, 4],
#                    [5, 6, 7, 8]])
#
# matriz[:] = 1
#
# print("Matriz ativa:")
# print(matriz)

#---------------------------------------------------
# Ex 7 ->
import numpy as np

matriz = np.array([[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]])

print("Antes:")
print(matriz)

matriz[0, 1] = 999
matriz[2, 4] = 888

print("Depois:")
print(matriz)