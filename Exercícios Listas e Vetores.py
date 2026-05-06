# EXERCICIOS LISTAS

# Ex 1 ->
lista = [1, 2, 3, 4, 5]
print(lista)

#---------------------------------------------------
# Ex 2 ->
# cores = ['vermelho', 'azul', 'verde', 'amarelo']
# print(cores[1])

#---------------------------------------------------
# Ex 3 ->
# numeros = [1, 2, 3]
# numeros.append(10)
# print(numeros)

#---------------------------------------------------
# Ex 4 ->
# frutas = ['maçã', 'banana', 'laranja']
# frutas.remove('banana')
# print(frutas)

#---------------------------------------------------
# Ex 5 ->
# itens = [10, 20, 30, 40, 50]
# print(len(itens))

#---------------------------------------------------
# Ex 6 ->
# valores = [1, 3, 5, 7, 9]
# print(7 in valores)

#---------------------------------------------------
# Ex 7 ->
# lista1 = [1, 2]
# lista2 = [3, 4]
# lista3 = lista1 + lista2
# print(lista3)

#---------------------------------------------------
# Ex 8 ->
# letras = ['a', 'b', 'c', 'd']
# letras.reverse()
# print(letras)

#---------------------------------------------------
# Ex 9 ->
# numeros = [1, 2, 2, 3, 2, 4]
# print(numeros.count(2))

#---------------------------------------------------
# Ex 10 ->
# precos = [10.5, 20.0, 15.5]
# print(sum(precos))

#---------------------------------------------------
# Ex 11 ->
# lista = [1, 2, 2, 3, 4, 3, 5]
# nova_lista = []
# for i in lista:
#     if i not in nova_lista:
#         nova_lista.append(i)
# print(nova_lista)

#---------------------------------------------------
# Ex 12 ->
# lista = [10, 5, 20, 2, 30]
# maior = lista[0]
# menor = lista[0]
# for i in lista:
#     if i > maior:
#         maior = i
#     if i < menor:
#         menor = i
# print("Maior:", maior)
# print("Menor:", menor)

#---------------------------------------------------
# Ex 13 ->
# quadrados = [x**2 for x in range(1, 11)]
# print(quadrados)

#---------------------------------------------------
# Ex 14 ->
# lista = [1, 2, 3, 4, 5, 6]
# impares = [x for x in lista if x % 2 != 0]
# print(impares)

#---------------------------------------------------
# Ex 15 ->
# lista = [1, 2, 3, 4, 5]
# n = 2
# resultado = lista[-n:] + lista[:-n]
# print(resultado)

#---------------------------------------------------
# Ex 16 ->
# lista1 = [1, 2, 3, 4]
# lista2 = [3, 4, 5, 6]
# intersecao = []
# for i in lista1:
#     if i in lista2 and i not in intersecao:
#         intersecao.append(i)
# print(intersecao)

#---------------------------------------------------
# Ex 17 ->
# matriz = [[1, 2], [3, 4]]
# resultado = []
# for sublista in matriz:
#     for item in sublista:
#         resultado.append(item)
# print(resultado)

#---------------------------------------------------
# Ex 18 ->
# def merge_sort(lista):
#     if len(lista) <= 1:
#         return lista
#     meio = len(lista) // 2
#     esquerda = merge_sort(lista[:meio])
#     direita = merge_sort(lista[meio:])
#     return merge(esquerda, direita)
#
# def merge(esq, dir):
#     resultado = []
#     i = j = 0
#     while i < len(esq) and j < len(dir):
#         if esq[i] < dir[j]:
#             resultado.append(esq[i])
#             i += 1
#         else:
#             resultado.append(dir[j])
#             j += 1
#     resultado.extend(esq[i:])
#     resultado.extend(dir[j:])
#     return resultado
#
# lista = [5, 2, 9, 1, 5, 6]
# print(merge_sort(lista))

#---------------------------------------------------
# Ex 19 ->
# lista = [3, -2, 5, -1]
# max_atual = max_global = lista[0]
# for i in range(1, len(lista)):
#     max_atual = max(lista[i], max_atual + lista[i])
#     if max_atual > max_global:
#         max_global = max_atual
# print(max_global)

#---------------------------------------------------
# Ex 20 ->
# def permutacoes(lista):
#     if len(lista) == 0:
#         return [[]]
#     resultado = []
#     for i in range(len(lista)):
#         resto = lista[:i] + lista[i+1:]
#         for p in permutacoes(resto):
#             resultado.append([lista[i]] + p)
#     return resultado
#
# lista = [1, 2, 3]
# print(permutacoes(lista))