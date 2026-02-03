def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = list(powers_of_2(8))
print(t) 

def powers_of_2b(n):
    powers = 1
    for i in range(n):
        yield powers
        powers *= 2
 
 
t = [x for x in powers_of_2b(8)]
print(t) 