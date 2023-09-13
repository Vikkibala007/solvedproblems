print("Enter the elements")
unknown=[]
n=int(input("Enter no of students"))
for i in range (0,n):
    nikki=int(input("Enter a value"))
    unknown.append(nikki)
print(unknown)
known=[]
for i in unknown:
    if i>=45:
        known.append("pass")
    elif i==16:
        known.append("perfect pass")
    else:
        known.append("fail")
print(known)
        

                
    

    



























































































