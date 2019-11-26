def longest_subsequence(arr, f):
    dp = [1] * n
    choice = [None] * n
    max_index = 0
    max_value = 1
    for i in xrange(1, n):
        curr_choice = None
        for j in xrange(i - 1, -1, -1):
            if f(arr[i], arr[j]) and 1 + dp[j] > dp[i]:
                dp[i] = 1 + dp[j]
                curr_choice = j
        choice[i] = curr_choice
        if dp[i] > max_value:
            max_value = dp[i]
            max_index = i

    answer = []
    while max_index >= 0:
        answer.append(arr[max_index])
        max_index = choice[max_index]
    return " ".join(map(str, answer[::-1]))
    


f = open("rosalind_lgis.txt", "r")
n = int(f.readline())
arr = map(int, f.readline().rstrip().split())

print longest_subsequence(arr, lambda x, y : x > y)
print longest_subsequence(arr, lambda x, y : x < y)