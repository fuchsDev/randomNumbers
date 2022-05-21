from random import randint
numeroAleatorio = int (randint (1,10))

#Menu Inicial
print("\n******************* Python Chute um Numero *******************")
print("\nA sorte foi lançada, advinhe o numero:")

chute = 0
tentativas = 0

while chute != numeroAleatorio:
   chute = int(input('Dê o seu "chute": '))
   tentativas += 1
   if chute == numeroAleatorio:
       print(('-'*25),'\nPARABÊNS','!!\n', 'você acertou com ', tentativas, 'tentativas') #'-'*25 faz repetir o caracter x25
   elif chute < numeroAleatorio:
       print('ERRADO!! chute um valor maior que', chute, '!')
   else:
       print('ERRADO!! chute um valor menor que',chute, '!')
print('_'*25)
   
print( '* Fim de jogo! *')
    
        