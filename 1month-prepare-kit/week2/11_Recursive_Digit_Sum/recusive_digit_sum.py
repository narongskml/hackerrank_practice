
def superDigit(n, k):
    # Write your code here
   if len(str(k)) == 1:
      if (n==1):   
         return int(k)   #k is one digit and n=1 return
      else:
         k=n*k     #case k is one digit   reduce formular with multiply and reset n =1
         n=1      

   total = sum(int(i) for i in str(k)) * n
   return superDigit(1, str(total))

superDigit(9875,4)
