def main():
	n = int(input())
	start = max([n - 55, 1])
	for i in range(start, n):
		curr = i
		curr_sum = curr
		while(curr):
			curr_sum += curr%10
			curr //= 10
		if (curr_sum == n):
			print(i)
			return
	
	print(0)


main()
