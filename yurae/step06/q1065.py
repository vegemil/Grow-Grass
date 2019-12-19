def check(x):
	if (x < 100):
		return True
	diff = 10
	while (x >= 10):
		curr_diff = x%10 - (x//10)%10
		if (diff != 10 and curr_diff != diff):
			return False
		diff = curr_diff	
		x = x//10
	return True

def main():
	n = int(input())
	cnt = 0
	for i in range(1, n+1):
		if(check(i) == True):
			cnt = cnt + 1
	print(cnt)

if __name__ == "__main__":
	main()
