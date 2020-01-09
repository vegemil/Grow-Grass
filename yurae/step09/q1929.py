import sys, math

def main():
	m, n = map(int, sys.stdin.readline().split())
	vals = range(m, n+1)
	mx = n+1

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
	for el in res:
		print(el)

if __name__ == "__main__":
	main()
