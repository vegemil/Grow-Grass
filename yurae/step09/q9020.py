import sys, math

def main():
	mx = 10001

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

	t = int(sys.stdin.readline())
	for _ in range(t):
		n = int(sys.stdin.readline())
		for i in range(n//2, 1, -1):
			if (arr[i] and arr[n-i]):
				print(i, n-i)
				break


if __name__ == "__main__":
	main()
