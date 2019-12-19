def get_next(curr):
	res = curr
	while (curr > 0):
		res = res + curr%10
		curr = curr//10
	return res

def main():
	rng = 10000
	check = [False for _ in range(rng+1)]

	for i in range(1, rng+1):
		if (check[i] == True):
			continue
		curr = get_next(i)
		while (curr <= rng):
			if (check[curr] == True):
				break
			check[curr] = True
			curr = get_next(curr)

	for i in range(1, rng+1):
		if (check[i] == True):
			continue
		print(i)

if __name__ == "__main__":
	main()
