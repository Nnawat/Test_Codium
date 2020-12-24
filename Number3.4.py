n = int(input("Enter a number : "))

star = int(n/2)
temp = 0 if n % 2 == 0 else 1
space = 0
space_in = n - 2
for row in range(star):
  txt = ""
  print((" " * space) + "*" + (" " * space_in) + "*" if n > 1 else "")

  space += 1
  space_in -= 2

txt = (" " * star) + "*" if temp == 1 else ""
if txt:
  print(txt)

space = star - 1
space_in = 0 if n % 2 == 0 else 1
for row in range(star):
  txt = ""
  print((" " * space) + "*" + (" " * space_in) + "*" if n > 1 else "")

  space -= 1
  space_in += 2
