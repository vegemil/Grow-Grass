import sys, math

def main():
	mx = 2*123456 + 1

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

	while(True):
		n = int(sys.stdin.readline())
		if (n == 0):
			return
		vals = range(n+1, 2*n+1)

		res = list(filter(lambda x: arr[x], vals))
		print(len(res))

if __name__ == "__main__":
	main()
