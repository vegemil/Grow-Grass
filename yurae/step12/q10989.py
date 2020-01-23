import sys

def main():
	n = int(sys.stdin.readline())

	cnt = [0 for _ in range(10001)]
	for _ in range(n):
		cnt[int(sys.stdin.readline())] += 1

	for i in range(1, len(cnt)):
		for _ in range(cnt[i]):
			print(i)


if __name__ == "__main__":
	main()

