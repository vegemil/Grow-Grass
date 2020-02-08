import sys

def main():
	n = int(input())
	if (n == 1):
		print(1)
		return
	elif (n == 2):
		print(2)
		return

	cnt1 = 1
	cnt2 = 2
	for i in range(3, n+1):
		cnt1, cnt2 = cnt2%15746, (cnt1+cnt2)%15746

	print(cnt2%15746)


if __name__ == "__main__":
	main()
