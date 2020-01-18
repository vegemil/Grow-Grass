def fact(n):
	if (n == 0):
		return 0
	elif (n == 1):
		return n
	else:
		return n*fact(n-1)


def main():
	print(fact(int(input())))


if __name__ == "__main__":
	main()
