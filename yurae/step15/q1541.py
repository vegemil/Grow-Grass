line = input().replace("+", " + ").replace("-", " - ").split()
is_plus = True
cnt = 0

for el in line:
	if el == "-":
		is_plus = False
	elif el == "+":
		continue
	else:
		if is_plus:
			cnt += int(el)
		else:
			cnt -= int(el)

print(cnt)
