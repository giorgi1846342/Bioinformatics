f = open('rosalind_gc.txt', 'r')
fasta = f.read().split('\n')
n = len(fasta)
fasta_dict = {}

for i in range(n):
    if i%2 == 0:
        fasta_dict[fasta[i]] = fasta[i+1]
        
percentage_lst = []      
for key in fasta_dict:
    dna_string = fasta_dict[key]
    if len(dna_string) != 0:
        relative_freq_gc = (dna_string.count('G') + dna_string.count('C'))/len(dna_string)
        percentage_gc = relative_freq_gc*100
        percentage_lst.append(percentage_gc)
    
highest_gc = max(percentage_lst)

print(list(fasta_dict.keys())[percentage_lst.index(highest_gc)], '\n', highest_gc)