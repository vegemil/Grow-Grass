import sys, math

def main():
	mx = 10001
	m = int(sys.stdin.readline())
	n = int(sys.stdin.readline())
	vals = range(m, n+1)

	arr = [True for _ in range(mx)]
	arr[0] = False
	arr[1] = False
	for i in range(2, int(math.sqrt(mx)+1)):
		chk = i*i
		if (arr[chk] == False):
			continue
		while (chk < mx):
			arr[chk] = False
			chk += i

	res = list(filter(lambda x: arr[x], vals))
	if not res:
		print(-1)
	else:
		print(sum(res))
		print(res[0])

if __name__ == "__main__":
	main()
