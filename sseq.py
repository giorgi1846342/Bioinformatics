with open('rosalind_sseq.txt', 'r') as file:
    text = file.read()

dna_list = []

items = text.split('>')

for item in items[1:]:
    item = item.split('\n')
    string_id = item.pop(0)
    dna_list.append(''.join(item))
    
s = dna_list[0]
t = dna_list[1]

res = []
i = j = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        res.append(i + 1)
        j += 1
    i += 1

print(*res)