nprime = int(input("Enter a number to check prime number: ")) 
print(nprime, "->", end=" ")   
for n in range(nprime + 1):  
   if n > 1:  
       for i in range(2,n):  
           if (n % i) == 0:  
              break  
       else:  
           print(n , end=" ")
