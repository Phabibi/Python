# Assignment 6 F
# Vowels
# Parsa Habibi



def searchVowel(st):
    i=0
    V='aeiouAEIOU'
    found=False
    while i<len(st) and found==False:
        if st[i] in V:
            found=True
        i+=1
    return found 
print(searchVowel("----a----"))
