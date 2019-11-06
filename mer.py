def merge_sort(A, B):
    i = 0
    j = 0
    sorted_list = []
    
    while len(A) >i and len(B) >j:
        if A[i] < B[j]:
            sorted_list.append(A[i])
            i +=1
        else:
            sorted_list.append(B[j])
            j +=1
            
    while i < len(A):
            sorted_list.append(A[i])
            i+=1

    while j < len(B):
            sorted_list.append(B[j])
            j +=1
            
    return sorted_list
    

with open("./rosalind_mer.txt", "r") as file:
    input_list = file.read().split("\n")
    A = list(map(int, input_list[1].split()))
    B = list(map(int, input_list[3].split()))
    
    
print(*merge_sort(A,B))