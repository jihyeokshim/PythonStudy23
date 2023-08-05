def solve(k):
    ans = []
    for i in range(1, k + 1):
        ans.append(i * i)
    return ans


n = int(input())
print(solve(n))
