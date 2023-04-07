#CÓDIGO COMENTADO EXPLICATIVO DE FUNÇÕES RECURSIVAS DO PROFESSOR GALILEU

notas = [200, 100, 50, 20, 10, 5, 2, 1]  #valores das notas disponíveis
caixa = [2, 0, 0, 0, 0, 0, 0, 0]        #quantidade de cada nota disponível no caixa
troco = 200                             #valor do troco a ser dado

#função recursiva para calcular o troco
def darTroco(caixa, troco, posNota):
    if posNota < len(notas):
        nota = notas[posNota]           #seleciona a nota atual
        maxNotas = caixa[posNota] + 1   #calcula a quantidade máxima dessa nota que pode ser usada
        for n in range(maxNotas):
            notasTroco = [0] * len(notas) #inicializa a lista de notas usadas no troco
            notasTroco[posNota] = n      #define a quantidade da nota atual usada no troco
            novoTroco = troco - n * nota #calcula o novo valor do troco após usar "n" notas

            if novoTroco != 0:
                #chama a função recursivamente para as próximas notas disponíveis
                darTroco(caixa, novoTroco, posNota + 1)
            else:
                #quando o troco foi totalmente dado, imprime as notas usadas
                notasUsadas(notasTroco)
                break

#função para imprimir as notas usadas no troco
def notasUsadas(notasTroco):
    for i in range(len(notasTroco)):
        if notasTroco[i] > 0:
            print(f"{notasTroco[i]} nota(s) de {notas[i]}")

#chama a função darTroco para iniciar o processo
darTroco(caixa, troco, 0)
