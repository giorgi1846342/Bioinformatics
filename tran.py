with open('rosalind_tran.txt', 'r') as file:
    text = file.read()

dna_dict = {}

items = text.split('>')

for item in items[1:]:
    item = item.split('\n')
    string_id = item.pop(0)
    dna_dict[string_id] = ''.join(item)
    
dna_list = []
for string in dna_dict.values():
    dna_list.append(string)

s = dna_list[0]
t = dna_list[1]

transition = 0
transversion = 0

for i in range(len(s)):
    
    if s[i] == 'A' and t[i] == 'G':
        transition += 1
    elif s[i] == 'G' and t[i] == 'A':
        transition += 1
    elif s[i] == 'C' and t[i] == 'T':
        transition += 1
    elif s[i] == 'T' and t[i] == 'C':
        transition += 1
        
    elif s[i] == 'A' and (t[i] == 'C' or  t[i] == 'T'):
        transversion += 1
    elif s[i] == 'G' and (t[i] == 'T' or  t[i] == 'C'):
        transversion += 1
    elif s[i] == 'C' and (t[i] == 'A' or  t[i] == 'G'):
        transversion += 1
    elif s[i] == 'T' and (t[i] == 'G' or  t[i] == 'A'):
        transversion += 1
        
ratio = transition / transversion
print(ratio)