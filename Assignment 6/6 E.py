# Assignment 6 E
# Pairs BOOL
# Parsa Habibi

def immPairsBool(st):
   n=False
   i=1
   while i<len(st) and not(n) :
      if st[i-1]==st[i]:
         n=True 
            
      i+=1
   return n
print(immPairsBool("x-x-"))
