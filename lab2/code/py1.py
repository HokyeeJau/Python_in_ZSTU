import numpy as np 

# import numpy as np

def check_num(n):
    try:
        float(n)
        return True
    except:
        return False 

if_number = True
number_list = []

print("Input starts...")
while if_number:
    num = input("Number: ")
    if_number = check_num(num)
    if if_number:
        number_list.append(float(num))

number_arr = np.array(number_list)
print("----------Analysis Report----------------")
print("Mean: "+'%-10.5s' % str(np.mean(number_arr)))
print("Std:  "+'%-10.5s' % str(np.std(number_arr)))
print("Std:  "+'%-10s' % str(np.median(number_arr)))