# Hoa Nguyen

# This program says hello world and ask for my language.
print('Hello world!')
print('Choose a language and I will greet you in that languge!') # ask for their language
print('1. Vietnamese')
print('2. Portuguese')
print('3. Turkish')
language = input()
if language == 'Vietnamese':
    print('Chao the gioi!')
if language == 'Portuguese':
    print('Ola Mundo!')
if language == 'Turkish':
    print('Selam Dunya!')
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

