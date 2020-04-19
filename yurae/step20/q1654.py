import sys	

def chk(arr, n, curr):	
	res = 0	
	if curr == 0:	
		return True	
	for el in arr:	
		res += el//curr	
	return res >= n	


def find(arr, n):	
	bot = 1	
	top = max(arr)	
	curr = (bot+top)//2	
	res = 0	
	while(True):	
		if bot > top:	
			break	
		chk_curr = chk(arr, n, curr)	
		if chk_curr:	
			res = curr	
			bot = curr+1	
			curr = (bot+top)//2	
		else:	
			top = curr-1	
			curr = (bot+top)//2	
	return res	


def main():	
	k, n = map(int, sys.stdin.readline().split())	
	arr = []	
	for _ in range(k):	
		arr.append(int(sys.stdin.readline()))	
	print(find(arr, n))	



if __name__ == "__main__":	
	main()
