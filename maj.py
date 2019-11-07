f = open('rosalind_maj.txt', 'r')
head = f.readline().strip().split()
length = int(head[1])
arrays = []
for line in f:
	array = line.strip().split()
	for x in array:
		x = int(x)
	arrays.append(array)

majority_elements = []
for array in arrays:
	for number in range(len(array)):
		count = 1
		if number > len(array)/2:
			majority_elements.append(-1)
			break
		for successive_number in range(number+1,len(array)):
			if array[number] == array[successive_number]:
				count +=1
		if count > len(array)/2:
			majority_elements.append(array[number])
			break
            
p = ''
for x in majority_elements:
    p += str(x) + ' '
print(p)	  