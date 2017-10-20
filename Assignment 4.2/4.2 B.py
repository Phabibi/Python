# Assingment 4.2 B 
# Count Digits
# Parsa Habibi

def count_digits(s):
    ans=""
    for k in range(len(s)):
        if s[k].isdigit():
            ans=ans+s[k]
    return len(ans)
s = "..1...1...1...1..."
print (count_digits(s))
 

            

