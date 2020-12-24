n = int(input("Enter a number : "))

space = n - 1
space_inside = -1

for row in range(n):
	txt = ""
	for space_do in range(space):
		txt += " "
	txt += "*"

	for space_inside_do in range(space_inside):
		txt += " "

	if row > 0:
		txt += "*"

	space -= 1
	space_inside += 2
	print(txt)