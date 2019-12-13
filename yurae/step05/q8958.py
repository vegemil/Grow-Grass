import sys

n = int(sys.stdin.readline())
for _ in range(n):
	line = sys.stdin.readline()
	cnt = 0
	curr = 1
	for i in range(0, len(line)):
		if (line[i] == "X"):
			curr = 1
			continue
		if (i > 0 and line[i-1] == line[i]):
			curr = curr + 1
		if (line[i] == "O"):
			cnt = cnt + curr
	print(cnt)
