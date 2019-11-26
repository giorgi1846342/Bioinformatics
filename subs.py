f = open('rosalind_subs.txt', 'r')
strings = f.read().split('\n')
s = strings[0]
t = strings[1]

res = [i for i in range(len(s)) if s.startswith(t, i)]

for i in range(len(res)):
    res[i] = res[i]+1
    
print(*res)