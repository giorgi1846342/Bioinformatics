f = open('rosalind_rna.txt', 'r')
rna = f.readline()

rna = rna.replace('T', 'U')

print(rna)