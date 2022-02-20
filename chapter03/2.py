n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse = True)
result = 0

# count = 0
# for _ in range(m):
#     if count < k:
#         result += data[0]
#         count += 1
#     else:
#         result += data[1]
#         count = 0

first = data[0]
second = data[1]

one_loop = first * k + second
num_loop = m // (k+1) # number of loops
rest = m % (k+1)
result = one_loop * num_loop + first * rest

print(result)