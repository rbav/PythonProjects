step_counter_list = []

for i in range(500):
    steps = 0
    n = i
    if i == 0:
        continue
    else:
        while n > 1:
            if n % 2 == 0:
                n = (n/2)
                #print(int(n))
                steps +=1
            else:
                n = ((n *3) + 1)
                steps +=1
                #print(int(n))
        step_counter_list.append(steps)
        print(steps)

with open('Collatz_hypothesis_steps.txt', 'w') as f:
    for line in step_counter_list:
        f.write(f"{line}\n")





        