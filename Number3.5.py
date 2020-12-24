n = int(input("Enter a number : "))

part_one = 1
part_two = 1

for part_one in range(n + 1):
    if part_one % 2 != 0:
        i = (n - part_one) // 2
        print (" "*i + "*"*(part_one) + " "*i ,end = "\n")

for part_two in range(n-1 ,0 ,-1):
    if part_two % 2 != 0:
        j = (n-part_two)//2
        print (" "*j + "*"*(part_two) + " "*j ,end = "\n")