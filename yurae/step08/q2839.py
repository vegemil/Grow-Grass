def main():
	n = int(input())
	if (n%5 == 0):
		print(n//5)
	else:
		for i in range(n//5, -1, -1):
			if ((n - i*5) % 3 == 0):
				print(i + (n - i*5)//3)
				return
		print(-1)

if __name__ == "__main__":
	main()
