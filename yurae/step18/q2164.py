import sys, math

n = int(sys.stdin.readline())
res = 2**int(math.log(n, 2))
if (n == res):
	print(res)
else:
	print(n*2 - res*2)
