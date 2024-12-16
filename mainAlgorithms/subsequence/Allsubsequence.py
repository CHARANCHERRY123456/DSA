arr =[1,2,3]
N = 3
def checkBit(i , j):
    return (i >> j) & 1

# it is possible to form 2**n subseqences
# consider them as binary numners
# if 0-not include , 1 - include
for i in range(2**N):
    sum = 0
    for j in range(N):
        # if checkBit at jth position in i is set then incldue it
        if (checkBit(i , j)):
            print(arr[j], end =" ")
    print()
