import sys

def compare(a, b):
	if(a[0] > b[0] and a[1] > b[1]):
		return 1
	elif(a[0] < b[0] and a[1] < b[1]):
		return -1
	else:
		return 0


def main():
	n = int(sys.stdin.readline())
	# [weight, height], grade
	arr = []
	for idx in range(n):
		x, y = map(int, sys.stdin.readline().split())
		arr.append([[x, y], 1])

	for i in range(n):
		for j in range(n):
			if (i == j):
				continue
			if(compare(arr[i][0], arr[j][0]) < 0):
				arr[i][1] += 1

	for el in arr[:-1]:
		print(el[1], end=" ")
	print(arr[-1][1])


main()
