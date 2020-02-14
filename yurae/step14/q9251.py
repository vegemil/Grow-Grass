def main():
	w1 = input()
	w2 = input()

	mx = 1001
	chk = [[0 for _ in range(mx)] for _ in range(mx)]

	for i in range(len(w1)):
		for j in range(len(w2)):
			if (w1[i] == w2[j]):
				chk[i][j] = 1 if (i == 0 or j == 0) else chk[i][j] + chk[i-1][j-1] + 1
			else:
				chk[i][j] = (0 if j == 0 else chk[i][j-1]) if i == 0 else (chk[i-1][j] if j == 0 else max([chk[i-1][j], chk[i][j-1]]))

	print(chk[i][j])	

if __name__ == "__main__":
	main()
