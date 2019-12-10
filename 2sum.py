f = open('rosalind_2sum.txt', 'r')
head = f.readline().strip().split()
arrays = []
for line in f:
	array = line.strip().split()
	for i in range(len(array)):
		array[i] = int(array[i])
	arrays.append(array)
	

for A in arrays:
    
    flag = False
    p = 0
    
    while p < len(A):
        q = p +1
        
        while q < len(A):
            
            if A[p] == -A[q]:
                
                print(p+1,q+1)
                
                flag = True
                p = len(A)
                q = len(A)
                
            q +=1
        p +=1
        
    if flag == False:
        print(-1)
