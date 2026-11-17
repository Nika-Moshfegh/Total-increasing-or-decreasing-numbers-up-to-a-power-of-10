def total_inc_dec(x):
    x=str(x)
    counter1=0
    counter2=0
    for i in range(0,len(x)-1):
        if x[i]>=x[i+1]:
            counter1+=1
        if x[i]<=x[i+1]:
            counter2+=1
     
    if counter1==len(x)-1:
        return "soody"
    if counter2==len(x)-1:
        return "Nozoly"
    return "we don't know about them"
    
cont=0
for i in range(101,200):
    if total_inc_dec(i)=="Nozoly" :
        cont+=1
        print("Nozoly: ",i)
    if total_inc_dec(i)=="soody":
        cont+=1
        print("soody: " , i)
        
print(cont)