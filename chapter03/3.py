n, m = map(int, input().split())
result = 0
for _ in range(n):
    temp = min(list(map(int, input().split())))
    result = max(result, temp)
    # if temp > result: result = temp

print(result)