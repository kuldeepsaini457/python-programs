def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

terms = int(input("Enter the number of terms in fibonacci series: "))

if terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(recur_fibo(i),end=" ")