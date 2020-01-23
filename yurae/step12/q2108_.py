import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []
sum = 0

for i in range(n):
    temp = int(sys.stdin.readline())
    li.append(temp)
    sum += temp

print('%.0f' %(sum/n))

if n == 1:
    print(li[0])
    print(li[0])
    print(0)
    sys.exit()

li = sorted(li)
print(li[n//2])

cnt = Counter(li)
cnt = sorted(cnt.items(), key=lambda x: (-x[1],x[0]))

if cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(int(li[-1]) - int(li[0]))


