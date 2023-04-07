S = "spam"

print(len(S)) #mostrar o tamanho de "S"
print(S[0]) #mostrando o primeiro indice de posição 0
print(S[1:3]) #definindo um intervalo que começa na posição 1 e vai até a posição 2
print(S + "xyz") #concatenação de SPAM com XYZ
print(S.find("pa")) #encontra a posição de "pa" em "S"
print(S.upper()) #converte S para maiúsculas
print(S.isalpha()) #verifica se os caracteres de "S" são alfabéticos
print(S.replace("pa", "ca")) #substitui a substring "pa" por "ca" em "S"

#REVISÃO DE LISTAS

L = [123, "casa", 3.14]
print(len(L)) #mostrar o tamanho da lista "L"
print(L[0]) #mostrando o primeiro elemento da lista "L" índice 0
print(L * 2) #repetindo a lista "L" duas vezes
L.append("bola") #adicionando a palavra "bola" ao final da lista "L"
print(L) #mostrando a lista "L"
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [n[1] for n in M] #extraindo a segunda coluna do índice 1 da matriz "M"
print(col2)

#REVISÃO DE DICIONÁRIOS

D = {"com": "ABC", "num": 23}
print(D["num"]) #acessando o valor associado a chave "num" no dicionário "D"
D["cor"] = "azul" #adicionando um novo par ao dicionário "D"
print(D) #mostrando o dicionário "D"
