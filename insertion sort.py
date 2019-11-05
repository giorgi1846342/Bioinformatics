with open("./rosalind_ins.txt", "r") as file:
    input_list = file.read().split('\n')
    n = int(input_list[0])
    string = input_list[1]
    l = list(map(int, string.split()))
    
    
def insertionSort(n, arr):
    count = 0
    for i in range(1, n):
        value = arr[i]
        j = i -1
        while j >= 0 and arr[j] > value:
            arr[j +1] = arr[j]
            count += 1
            j -= 1
        arr[j+1] = value
    return count
        
print(insertionSort(n, l))    