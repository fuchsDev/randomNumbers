#imports and variabes
from random import randint
randomNumber = int (randint (1,10))
bet = 0
attempts = 0

#menu
print("\n******************* Python Kick a Number *******************")
print("\nThe lot has been cast, guess the number from 1 to 10:")

#loop
while bet != randomNumber:
   bet = int(input('Of your "kick": '))
   attempts += 1
   if bet == randomNumber:
       print(('-'*25),'\nCONGRATULATIONS','!!\n', 'you got it right with ', attempts, ' tries')
   elif bet < randomNumber:
       print('WRONG!! you got it right with', bet, '!')
   else:
       print('WRONG!! guess a value less than',bet, '!')
print('_'*25)
   
print( '* End Game! *')