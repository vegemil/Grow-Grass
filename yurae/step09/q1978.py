import sys, math

def main():
	mx = 1001
	n = int(sys.stdin.readline())
	vals = list(map(int, sys.stdin.readline().split()))

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
	print(len(res))

if __name__ == "__main__":
	main()
