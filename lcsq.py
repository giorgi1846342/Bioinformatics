with open('rosalind_lcsq.txt', 'r') as file:
    text = file.read()

dna_list = []

items = text.split('>')

for item in items[1:]:
    item = item.split('\n')
    string_id = item.pop(0)
    dna_list.append(''.join(item))
    
s = dna_list[0]
t = dna_list[1]

lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

for i, x in enumerate(s):
    for j, y in enumerate(t):
        if x == y:
            lengths[i + 1][j + 1] = lengths[i][j] + 1
        else:
            lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

spliced_motif = ''
x, y = len(s), len(t)
while x * y != 0:
    if lengths[x][y] == lengths[x - 1][y]:
        x -= 1
    elif lengths[x][y] == lengths[x][y - 1]:
        y -= 1
    else:
        spliced_motif = s[x - 1] + spliced_motif
        x -= 1
        y -= 1
        
print(spliced_motif)