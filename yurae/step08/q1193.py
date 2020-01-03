import math

def main():
	x = int(input())
	cnt = 0
	cnt_after = 0
	for i in range(int(math.sqrt(x*2)), x+1):
		if ((i*(i+1))//2 >= x):
			cnt = i
			cnt_after = x - (i*(i-1))//2
			break

	res = ""
	if (cnt%2 == 0):
		res = str(cnt_after) + "/" + str(cnt + 1 - cnt_after)
	else:
		res = str(cnt + 1 - cnt_after) + "/" + str(cnt_after)

	print(res)


if __name__ == "__main__":
	main()
