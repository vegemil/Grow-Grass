import math

def main():
	n = int(input())
	if (n == 1):
		print(1)
		return

	tmp = int(math.sqrt((n-1)//3))
	for i in range(tmp, n+1):
		if (6*sum(range(i)) >= n-1):
			print(i)
			return

if __name__ == "__main__":
	main()
