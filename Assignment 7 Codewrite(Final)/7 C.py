# Assigment 7 C
# Mat Ddim x Dim
# Parsa Habibi

def createMatDimXDim (dim):
    a=[]
    i=0
    while i<dim:
        lista=[]
        for c in range(dim):
            lista+=a
        i+=1    
        return a.append([c+1]+lista)
print (createMatDimXDim (4))  
