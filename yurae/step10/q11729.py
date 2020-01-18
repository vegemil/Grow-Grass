def hanoi(n, steps, curr, target):
	if (n == 1):
		steps.append((curr, target))
		return 1
	else:
		nxt = 6 - (curr+target)
		return (hanoi(n-1, steps, curr, nxt) + hanoi(1, steps, curr, target) + hanoi(n-1, steps, nxt, target))


def main():
	n = int(input())
	steps = []
	print(hanoi(n, steps, 1, 3))
	for step in steps:
		print(step[0], step[1])


if __name__ == "__main__":
	main()
