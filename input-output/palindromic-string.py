import math
s = input()
if len(s) > 100:
    print ("Error! Only 100 characters allowed!")
    exit()
else:
    len_s = len(s)
    for i in range((math.ceil(len_s/2))):
        if (s[i] != s[len_s-i-1]):
            print('NO')
            break
    else:
        print('YES')