with open('rosalind_grph.txt', 'r') as file:
    text = file.read()

dna_dict = {}

items = text.split('>')

for item in items[1:]:
    item = item.split('\n')
    string_id = item.pop(0)
    dna_dict[string_id] = ''.join(item)

index = 0
for index, (key1, string1) in enumerate(dna_dict.items()):
    suffix = string1[-3:len(string1)]
    index +=1
    for index, (key2, string2) in enumerate(dna_dict.items()):
        prefix = string2[:3]
        if prefix == suffix and key1 != key2:
            print(key1, key2)