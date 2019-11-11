f = open('rosalind_3sum.txt', 'r')
input_file = f.read().split('\n')
nk = input_file[0].split()

k = int(nk[0])
n = int(nk[1])


for x in range(1, k+1):
    found = False
    array = input_file[x].split()

    numbers = {}
    for i in range(n):
        numbers[int(array[i])] = i

    for a in range(n):
        if found == True:
            break
        else:
            first = int(array[a])
        for b in range(a+1, n):
            second = int(array[b])
            if ((-1)*(first+second)) in numbers:
                c = numbers[(-1)*(first+second)]
                print(a+1, b+1, c+1)
                found = True
                break 
    if found == False:
        print('-1')