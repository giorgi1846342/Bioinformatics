f = open('rosalind_revc.txt', 'r')
dna = f.readline()
new_dna = []

for base in dna:
    if base == 'A':
        new_dna.append('T')
    elif base == 'T':
        new_dna.append('A')
    elif base == 'G':
        new_dna.append('C')
    elif base == 'C':
        new_dna.append('G')
    
new_dna = ''.join(reversed(new_dna))

print(new_dna)