import random

characters = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')

def space():
    print('')

createdkey = '[Error, nothing here yet]'
print('[Random key generator is ready]')

def createkey(amount):
    made = 0
    global createdkey
    createdkey = ''
    while amount > made:
        ranchar = random.choice(characters)
        createdkey = (f'{createdkey}{ranchar}')
        made = made + 1

    print(createdkey)

while True:
    keylength = float(input('[How many characters should the key be?] '))
    space()
    createkey(keylength)
    space()