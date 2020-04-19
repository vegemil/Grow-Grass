import sys

def main():
	n, k = map(int, sys.stdin.readline().split())
	arr = []
	for _ in range(n):
		arr.append(int(sys.stdin.readline()))

	arr.sort()
	chk = [0 for _ in range(k+1)]
	chk[0] = 1
	for el in arr:
		for i in range(el, k+1):
			chk[i] += chk[i-el]

	print(chk[k])


if __name__ == "__main__":
	main()
