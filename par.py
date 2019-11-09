def partition(arr):
    arr.append(arr.pop(0))
    start = 0
    end = len(arr)-1
    follower = leader = start
    while leader < end:
        if arr[leader] <= arr[end]:
            arr[follower], arr[leader] = arr[leader], arr[follower]
            follower += 1
        leader += 1
    arr[follower], arr[end] = arr[end], arr[follower]
    return arr
    
with open('./rosalind_par.txt', 'r') as file:
    input_list = file.read().split("\n")
    arr = list(map(int, input_list[1].split()))
    
print(*partition(arr))