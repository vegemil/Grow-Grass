import sys

res = 3000
def calc_diff(arr, picked):
	non_picked = [i for i in range(0, len(arr))]
	sum1 = 0
	sum2 = 0

	for i in picked:
		non_picked.remove(i)

	for i in picked:
		for j in picked:
			sum1 += arr[i][j]

	for i in non_picked:
		for j in non_picked:
			sum2 += arr[i][j]

	return abs(sum1 - sum2)

def pick(arr, picked, curr, to_pick):
	if (len(picked) >= to_pick):
		global res
		res = min(res, calc_diff(arr, picked))
		return
	
	for i in range(curr, len(arr)):
		if i in picked:
			continue
		picked.append(i)
		pick(arr, picked, i+1, to_pick)
		del picked[-1]


def main():
	n = int(sys.stdin.readline())
	arr = []
	for _ in range(n):
		arr.append(list(map(int, sys.stdin.readline().split())))

	global res
	pick(arr, [], 0, n//2)
	print(res)

if __name__ == "__main__":
	sys.setrecursionlimit(1000000)
	main()
