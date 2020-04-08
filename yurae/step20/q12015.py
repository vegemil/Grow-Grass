import sys

def pick(arr, minval):
	bot = 0
	top = len(arr)-1
	res = -1
	while(bot <= top):
		curr = (bot+top)//2
		if (arr[curr] >= minval):
			res = curr
			top = curr - 1
		else:
			bot = curr + 1
	return res


def main():
	n = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))

	cnt = [0]
	for el in arr:
		if (el > cnt[-1]):
			cnt.append(el)
		else:
			idx = pick(cnt, el)
			cnt[idx] = el
	print(len(cnt)-1)



if __name__ == "__main__":
	main()
