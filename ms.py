def merge_sort2(arr):
    
    if len(arr)>1:
        mid = len(arr)//2
        A = arr[:mid]
        B = arr[mid:]
        i = j = k = 0
        
        merge_sort2(A)
        merge_sort2(B)
        
        while len(A) >i and len(B) >j:
            if A[i] <= B[j]:
                arr[k] = A[i]
                i +=1
            else:
                arr[k] = B[j]
                j +=1
            k +=1
                
        while i < len(A):
                arr[k] = A[i]
                i +=1
                k +=1
    
        while j < len(B):
                arr[k] = B[j]
                j +=1
                k +=1
                
        return arr
    

with open("./rosalind_ms.txt", "r") as file:
    input_list = file.read().split("\n")
    arr = list(map(int, input_list[1].split()))
    
    
    
print(*merge_sort2(arr))