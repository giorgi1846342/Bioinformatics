with open('rosalind_pdst.txt', 'r') as file:
    text = file.read()

dna_list = []

items = text.split('>')

for item in items[1:]:
    item = item.split('\n')
    string_id = item.pop(0)
    dna_list.append(''.join(item))

count = 0

for i in dna_list:
    distance_matrix = []
    for j in dna_list:
        count = 0
        for base1, base2 in zip(i, j):
            if base1 != base2:
                count +=1
        distance_matrix.append(str.format('{0:.5f}', count / len(dna_list[0])))
    print(*distance_matrix, sep=' ')