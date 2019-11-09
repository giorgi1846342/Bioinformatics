def partition3(a):
   x, j, t = a[0], 0, len(a)-1
   i = j

   while i <= t :
      if a[i] < x:
         a[j], a[i] = a[i], a[j]
         j += 1

      elif a[i] > x:
         a[t], a[i] = a[i], a[t]
         t -= 1
         i -= 1
      i += 1   
   return a
    
with open('./rosalind_par3.txt', 'r') as file:
    input_list = file.read().split("\n")
    arr = list(map(int, input_list[1].split()))
    
print(*partition3(arr))