import sys

t = int(sys.stdin.readline())
for i in range(1, t+1):
	(a, b) = map(int, sys.stdin.readline().split())
	line = "Case #" + str(i) + ": " + str(a) + " + " + str(b) + " = " + str(a+b)
	print(line)
