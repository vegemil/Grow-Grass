import sys

n = int(sys.stdin.readline())
for _ in range(n):
	line = sys.stdin.readline().split()[0]
	cnt = 0
	is_valid = True
	for el in line:
		if el == "(":
			cnt += 1
		elif el == ")":
			if cnt < 1:
				is_valid = False
				break
			else:
				cnt -= 1
	if not is_valid or cnt > 0:
		print("NO")
	else:
		print("YES")
