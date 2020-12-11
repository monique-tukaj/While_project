print('''Type the phrases bellow to know our answer:
1. Hello
2. How are you?
3. Good bye''')
ps = (70 * '-') + '\nYou might have to try again if the phrases will be inserted differently.'
print(ps)

while True:
    userInput = str(input('Please input the choosen phrase: ')).upper()
    if userInput == 'HELLO':
        print('Hello to you too!')
    elif userInput == 'HOW ARE YOU?':
        print('Fine, thanks for asking.')
    elif userInput == 'GOOD BYE':
        break
    else:
        print('Try again.')