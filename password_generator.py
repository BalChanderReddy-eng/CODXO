## for making decesion randomly

import random

###importing string module

import string

##creting a function for generating random password
#the function has a length for password

def random_password(length = 15):

    ## this variable will contain all the string values to generate all the combinations of digits asciis etc
    combinealphabet = string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation





    password = ''.join(random.choice(combinealphabet) for i in range(length))


    return password

random_pass = random_password()

print(random_pass)
