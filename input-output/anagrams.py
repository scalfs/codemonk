t=input()
for i in range(int(t)):
    NumberOfDeletions=0
    a=input()
    b=input()

    if (len(a)>10000 or len(b)>10000):
        print("Error! Only 10000 character allowed.")
        exit()
    else:
        for letter in set(a):
            if letter in b:
                NumberOfDeletions+=abs(b.count(letter) - a.count(letter))
            else:
                NumberOfDeletions+=a.count(letter)

        for letter in set(b):
            if letter in a:
                continue
            else:
                NumberOfDeletions+=b.count(letter)
        print(NumberOfDeletions)