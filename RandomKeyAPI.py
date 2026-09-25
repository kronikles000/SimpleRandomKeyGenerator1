import random

characters = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')

#Beware this code may not be secure but you can build upon it.
#code by kronikles000 on Github use the code as you wish you can remove this note
global keylength

def createkey(amount):
    made = 0
    global createdkey
    createdkey = ''
    while amount > made:
        ranchar = random.choice(characters)
        createdkey = (f'{createdkey}{ranchar}')
        made = made + 1


createkey(keylength)

