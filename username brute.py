import itertools
from itertools import product
import sys
from string import ascii_lowercase

#url = "https://api.github.com/users/"

# none of this is neccessary, just testing shit
#sys.stdout = open("output.txt", "w")

#product (numbers,letters)
#for i in product(numbers,letters, repeat = 2):
#    print (url + str(i))

#sys.stdout.close()


sys.stdout = open("output.txt", "w")
keywords1 = [''.join(i) for i in itertools.product(ascii_lowercase)]
keywords2 = [''.join(i) for i in itertools.product(ascii_lowercase, repeat = 2)]
keywords3 = [''.join(i) for i in itertools.product(ascii_lowercase, repeat = 3)]



print (str(keywords1) + "\n" + str(keywords2) + "\n" + str(keywords3))

sys.stdout.close()

    

     





    
