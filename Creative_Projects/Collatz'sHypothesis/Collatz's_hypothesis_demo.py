n = int(input("Please enter any interger number above zero: "))

steps = 0
if n <= 1:
    exit
else:
    while n > 1:
        steps +=1
        if n % 2 == 0:
            n = (n/2)
            print(int(n))
        else:
            n = ((n *3) + 1)
            print(int(n))
print("Steps = ", steps)