import sys


def pick(nums, op, curr, res):
	if (len(nums) <= 0):
		res[0] = curr if curr > res[0] else res[0]
		res[1] = curr if curr < res[1] else res[1]
		return
	
	# plus
	if (op[0] > 0):
		op[0] -= 1
		pick(nums[1:], op, curr+nums[0], res)
		op[0] += 1
	# minus
	if (op[1] > 0):
		op[1] -= 1
		pick(nums[1:], op, curr-nums[0], res)
		op[1] += 1
	# multiply
	if (op[2] > 0):
		op[2] -= 1
		pick(nums[1:], op, curr*nums[0], res)
		op[2] += 1
	# divide
	if (op[3] > 0):
		op[3] -= 1
		if (curr < 0):
			pick(nums[1:], op, -((-curr)//nums[0]), res)
		else:
			pick(nums[1:], op, curr//nums[0], res)
		op[3] += 1



def main():
	n = int(sys.stdin.readline())
	nums = list(map(int, sys.stdin.readline().split()))
	# +, -, x, %
	op = list(map(int, sys.stdin.readline().split()))

	mx = -1000000000
	mn = 1000000000
	res = [mx, mn]

	pick(nums[1:], op, nums[0], res)
	print(res[0])
	print(res[1])


if __name__ == "__main__":
	sys.setrecursionlimit(1000000)
	main()
