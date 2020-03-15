from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1, n+1)])

cnt = 0
curr = 0
for target in targets:
	idx = deq.index(target)
	diff = abs(curr-idx)
	if (diff>len(deq)//2):
		cnt += len(deq) - (diff)
	else:
		cnt += (diff)
	del deq[idx]
	if (len(deq) != 0):
		curr = idx%len(deq)


print(cnt)
