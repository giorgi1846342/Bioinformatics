f = open('rosalind_hamm.txt', 'r')
strings = f.read().split('\n')
s = strings[0]
t = strings[1]

count = 0
for i in range(len(s)):
    if s[i] != t[i]:
        count +=1
            
print(count)