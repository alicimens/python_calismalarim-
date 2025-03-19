from functools  import reduce 

def  carp  (a,b) : 

    return a *b

sonuc   =  reduce (carp ,[1,2,3,4,5])

print (sonuc)