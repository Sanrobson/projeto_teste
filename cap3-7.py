# Solução do Problema referente ao Capitulo 3, questao 3.6

pessoas = ['andressa', 'aninha', 'wesley']
pessoas[2] = "felipe"  # inseri felipe
pessoas.insert(0, 'alex')  # inseri na posiçao 0 a pessoa alex
pessoas.insert(2, 'gil')  # inseri na posiçao 2 a pessoa gil
pessoas.append('swelton')  # inseri na ultima posiçao a pessoa swelton

print("Informamos que devido problemas tecnicos, só poderemos convidar duas pessoas.")
print(pessoas)  # aqui mostra a lista de pessoas.

desconvidados = pessoas.pop(0), pessoas.pop(1), pessoas.pop(2), pessoas.pop()
# comando pop sem paramento, remove por padrão o ultimo da list
print("Desculpe-nos " + str(desconvidados) +
      " sentimos muito por não poder convida-los mais.")

convidados = pessoas

mensagem = "olá " + str(convidados) + " Sejam bem vindos ao jantar !"
print(mensagem)  # vai mostrar as pessoas da lista que nao foram excluidas

del convidados[1]  # exclui a pessoa 1
del convidados[0]  # exclui a pessoa 2

print(pessoas)  # apresenta lista vazia.
