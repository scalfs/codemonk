n = int(input())
A = input()
if n > 1000:
    print ("Error! Only 1000 elements allowed!")
    exit()
else:
    answer = 1
    e = 10**9+7
    A = A.split(' ')
    for i in A:
        answer = (answer*int(i))%e
    print(answer)