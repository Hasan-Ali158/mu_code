from array import array
import random

ar=array("f",[1,22,3,4,5,6,])

for i in range(len(ar)):
    ar[i]=random.random()

ar[1]=-333
ar[2]=False
ar[3]=22.2

for value in ar:
    print(value)

