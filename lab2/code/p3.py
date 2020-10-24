import random
import string


randint = lambda x: random.randint(0, x)
alphabet = list(string.ascii_letters) 
number = list(range(0, 10))

def generate_random_pwd():
    random.shuffle(alphabet)
    random.shuffle(number)
    
    password = [0] * 10
    for i in range(0, 10):
        n = randint(len(alphabet)-1)
        password[i] = alphabet[n]

    password[randint(9)] = str(number[randint(9)])
    password[randint(9)] = str(number[randint(9)])
    return "".join(password)

for i in range(1, 11):
    print("Password "+str(i)+" :"+generate_random_pwd())