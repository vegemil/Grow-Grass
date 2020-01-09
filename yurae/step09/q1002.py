import sys, math

def main():
	t = int(sys.stdin.readline())
	for _ in range(t):
		x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
		if (x1 == x2 and y1 == y2):
			if (r1 == r2):
				print(-1)
			else:
				print(0)
			continue
		if (r1 > r2):
			r1, r2 = r2, r1

		dist = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
		if (dist > r1 + r2):
			print(0)
		elif (dist == r1 + r2):
			print(1)
		else:
			if (dist + r1 < r2):
				print(0)
			elif (dist + r1 == r2):
				print(1)
			else:
				print(2)


main()
