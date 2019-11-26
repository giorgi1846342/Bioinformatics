from Bio import SeqIO                                                   
handle = open('rosalind_revp.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
     sequence = []                         
     for nt in record.seq:                 
          sequence.extend(nt)                          
handle.close()
string = ''.join(sequence)
print(string)

def reverse(string):
    new_dna = []
    for base in string:
        if base == 'A':
            new_dna.append('T')
        elif base == 'T':
            new_dna.append('A')
        elif base == 'G':
            new_dna.append('C')
        elif base == 'C':
            new_dna.append('G')
        
    reverse = ''.join(reversed(new_dna))
    return reverse
print(reverse(string))

results = []

l = len(string)

for i in range(l):
    for j in range(4, 13):

        if i + j > l:
            continue

        s1 = string[i:i+j]
        s2 = reverse(s1)

        if s1 == s2:
            results.append((i + 1, j))

for i in results:
    print(*i)