#User define number range

distance_list = []
prime_list = []
ntemp = 0
num2 = int(input("Enter a terminal number please:" ))

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, num2):
    if is_prime(i + 1):
        #print(i + 1, end=" ")
        prime_list.append(i+1)

#print(prime_list)


for n in prime_list:
    if n >= 3:
        distance = n - ntemp
    else:
        distance = n - 1
    distance_list.append(distance)
    ntemp = n

#print(distance_list)

with open('Prime_number.txt', 'w') as f:
    for line in prime_list:
        f.write(f"{line}\n")