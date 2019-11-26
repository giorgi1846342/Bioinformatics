from itertools import product

with open('rosalind_lexf.txt', 'r') as file:
    input_file = file.read().split('\n')
    letters = input_file[0].split()
    n = int(input_file[1])
    
for x in product(letters, repeat=n):
    print (''.join(x))