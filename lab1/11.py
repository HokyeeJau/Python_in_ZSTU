num = input("Enter a number between 0 and 1000:")
if num[0] == '-' or len(num)>3:
    print("Wrong number!")
else:
    summ = 0
    for i in num:
        summ += int(i)
    print("The sum of the digits is",summ)