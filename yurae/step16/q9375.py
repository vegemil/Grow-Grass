import sys

def main():
	t = int(sys.stdin.readline())
	for _ in range(t):
		n = int(sys.stdin.readline())
		clothes = {}
		for _ in range(n):
			name, key = sys.stdin.readline().split()
			if key in clothes:
				clothes[key] += 1
			else:
				clothes[key] = 2

		cnt = 1
		for el in clothes:
			cnt *= clothes[el]
		print(cnt-1)


if __name__ == "__main__":
	main()
