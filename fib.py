f = open('rosalind_fib.txt', 'r')
f = f.read().split()
n = int(f[0])
k = int(f[1])

rabbits_alive = [1, k +1]
for _ in range (n-2):
    offspring = k * rabbits_alive[-2]
    rabbits_alive.append(offspring + rabbits_alive[-1])

print(rabbits_alive[-2])