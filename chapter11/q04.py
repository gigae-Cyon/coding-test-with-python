# -*- coding: utf-8 -*-
"""Q04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XBYvG--C9Z7DDIeCDuwJe3D1PufCBvD1
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt = 1

# for i in range(n):
#   if cnt >= data[i]:
#     cnt += data[i]
#   else:
#     break

# enhanced code
for x in data:
  if cnt < x:
    break
  cnt += x
    
print(cnt)

################
# wrong answer #
################

# count = 1
# while 1:
#   temp = count
#   for datum in data:
#     if temp >= datum:
#       temp -= datum
#   if temp == 0:
#     count += 1
#   else:
#     break

# print(count)