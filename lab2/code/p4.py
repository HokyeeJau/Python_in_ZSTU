import time

list_start =time.clock()
arr = [1,2,3,4,5,6,7]
if 1 in arr:
    print("Yes")
else:
    print("No")
list_end = time.clock()
print('List running time: %s Seconds'%(list_end-list_start))

set_start =time.clock()
s = set([1,2,3,4,5,6,7])
if 1 in s:
    print("Yes")
else:
    print("No")
set_end = time.clock()
print('Set running time: %s Seconds'%(set_end-set_start))
