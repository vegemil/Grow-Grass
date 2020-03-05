import sys

stk = []
k = int(sys.stdin.readline())
for _ in range(k):
	n = int(sys.stdin.readline())
	if (n == 0):
		stk.pop()
	else:
		stk.append(n)
print(sum(stk))
