s = input()
if len(s) > 100:
    print ("Error! Only 100 characters allowed!")
    exit()
else:
    print(s.swapcase())