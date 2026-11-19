def total_inc_dec(x):
    if x==0:
        return 1
    
    start=0
    end=(10**x) -1
        
    x=str(x)
    counter1=0
    counter2=0
    for i in range(0,end):
        if x[i]>=x[i+1]:
            counter1+=1
        if x[i]<=x[i+1]:
            counter2+=1
     
    if counter1==len(x)-1:
        return "soody"
    if counter2==len(x)-1:
        return "Nozoly"
    return "we don't know about them"
    
# cont=0
# for i in range(101,200):
#     if total_inc_dec(i)=="Nozoly" :
#         cont+=1
#         print("Nozoly: ",i)
#     if total_inc_dec(i)=="soody":
#         cont+=1
#         print("soody: " , i)
        
# print(cont)

def  total_inc_dec2(x):
    x=str(x)
    
    return x in "123456790"
    
print(
total_inc_dec2(123)
)



