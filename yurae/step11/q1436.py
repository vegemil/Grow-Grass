def main():
	n = int(input())
	idx = 0
	for i in range(666, 6000000):
		flag = 0
		curr = i
		while (curr):
			if (curr%10 == 6):
				flag += 1
				if (flag >= 3):
					idx += 1
					if (idx == n):
						print(i)
						return
					break
			else:
				flag = 0
			curr //= 10



main()
