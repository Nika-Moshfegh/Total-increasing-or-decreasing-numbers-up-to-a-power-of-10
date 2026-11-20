def total_inc_dec(x):
    if x==0: return 1
    
    end=(10**x)
    counter=0
    
    for i in range(0,end):
        tmp=str(i)
        if tmp==''.join(sorted(tmp)) or tmp==''.join(sorted(tmp,reverse=True)): counter+=1
    
    return counter        
    
print(
    total_inc_dec(5)    
)


