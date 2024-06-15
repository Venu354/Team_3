def printPatt(n):
    ans = []
    star = "*" * n
    for i in range(n):
        ans.append(star[:n - i])
    return ans

n = 5
ans = printPatt(n)
print(ans)

