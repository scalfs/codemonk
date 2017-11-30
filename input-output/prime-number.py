n = int(input(""))
if n > 1000:
    print ("Error! Max 1000!")
    exit()
else:
    for num in range(2,n):
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print(num, end=' ')