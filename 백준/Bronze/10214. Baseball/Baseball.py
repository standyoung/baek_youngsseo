T = int(input())

y_sc = 0
k_sc = 0
for _ in range(T):
	for _ in range(9):
		y, k = map(int, input().split())
		y_sc += y
		k_sc += k

	if y_sc > k_sc:
		print("Yonsei")
	elif y_sc < k_sc:
		print("Korea")
	else:
		print("Draw")