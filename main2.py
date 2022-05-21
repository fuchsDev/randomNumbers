from random import randint

#Menu Inicial
print("\n******************* Python Simulador de Dado *******************")
print("\nDeseja atirar o dado? (s / n)")
escolha = str(input("Digite s para Sim ou n para Não: "))

while (escolha != 'n'): #inicia o loop se for digitado 's'
    if escolha == 's':
        dado = randint(1,6)
        print("Você escolheu jogar o dado, e o numero gerado foi:")
        print(dado)
        escolha = str(input("Deseja continuar?(s/n)"))
    else:
        print("opção invalida")
        break
 
'''
from random import randint
n = int (randint (1,200))
p = 0
t = 0
nome = input ('Qual seu nome?')
while p != n:
   p = int(input('Dê o seu Palpite!'))
   t += 1
   if p==n:
       print(('-'*25),'\nPARABÊNS',nome,'!!\n', 'você acertou com ', t, 'tentativas')
   elif p < n:
       print('ERRADO!! chute um valor maior que', p, '!')
   else:
       print('ERRADO!! chute um valor menor que',p, '!')
print('_'*25)
   
print( '* Fim de jogo! *')
'''
    
        