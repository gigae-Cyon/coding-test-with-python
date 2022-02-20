n, k = map(int, input().split())

# result = 0
# while n != 1:
#     if n % k == 0:
#         n = n // k
#     else:
#         n -= 1
#     result += 1

# wrong answer
# result = n // k
# result += n % k

result = 0
while n >= k:
    target = (n // k) * k
    result += n - target
    n = target
    while n % k == 0:
        n //= k
        result += 1
result += n-1

print(result)