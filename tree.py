adjacency_list = []                                          
with open('rosalind_tree.txt', 'r') as f:             
    for line in f:                                 
        split_data = [int(x) for x in line.split()]
        adjacency_list.append(split_data)
        
n = adjacency_list[0][0]                                     
edges = adjacency_list[1:]                                   
print(n - len(edges) - 1)
