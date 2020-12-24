def leapyear(n):
    
    if 0 == n % 4 and 0 != n % 100 or 0 == n % 400: 
      print(n,"-> true")
    
    else:
      print(n,"-> false")

n = int(input("Enter a number of year: "))
leapyear(n)
