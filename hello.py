import random
from flafla import printGreen,printRed

char = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
test = 'abcd'+random.choice(char)+random.choice(number)*3

printGreen('test')
printRed('test')