# Solução do Problema referente ao Capítulo 3, questão 3.6

jantar = ['Ro', 'Mauro', 'Marcos']
jantar.insert(0, "Lucas")
jantar.insert(2, "Lais")
jantar.append("Robson")

message0 = "Olá Amigo hoje tem salada vc gosta " + jantar[0] + "?"
message1 = "Tem carne e peixe oque vc vai querer " + jantar[1] + " ?"
message2 = "Deixa espaço para sobremesa " + jantar[2] + "."
message3 = "Olá " + jantar[3] + " Vc gosta de salada ? "
message4 = "Olá " + jantar[4] + " Vc gosta de sorvete ? "
message5 = "Olá " + jantar[5] + " Vc ja almoçou ? "

print("  \n " + message0 + " \n " + message1 +
      " \n " + message2 + "\n " + message3 + "\n " + message4 + "\n " + message5)
