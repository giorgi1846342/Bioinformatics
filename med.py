def med(arr, n, k):
    arr.sort()
    return arr[k-1]
    
with open('./rosalind_med.txt', 'r') as file:
    input_list = file.read().split("\n")
    n = int(input_list[0])
    arr = list(map(int, input_list[1].split()))
    k = int(input_list[2])

print(med(arr, n, k))