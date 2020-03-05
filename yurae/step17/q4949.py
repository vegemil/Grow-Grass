while(True):
	line = input()
	if line == ".":
		break
	stk = []
	is_valid = True
	for el in line:
		if el == "[":
			stk.append(0)
		elif el == "(":
			stk.append(1)
		elif el == "]":
			if not stk or stk.pop() != 0:
				is_valid = False
				break
		elif el == ")":
			if not stk or stk.pop() != 1:
				is_valid = False
				break
	if not is_valid or len(stk) > 0:
		print("no")
	else:
		print("yes")
