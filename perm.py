from itertools import permutations

with open('rosalind_perm.txt', 'r') as file:
    input_file = file.read()
    n = int(input_file)
    
l = []
for i in range(n):
    l.append(i+1)
    
results = list(permutations(l))

print(len(results))

for i in results:
    print(*i)