#Variable Assignment

var1='python'
print('Variable 1 =',var1)         #Simple assignment of a variable

print(type(var1),id(var1))  #there is an ID assigned to every variable

var2=var3=var4='India'
print(id(var2),id(var3),id(var4))   #If you assign multiple variables in one line, they all will have the same ID

var3='USA'
print(var3, id(var3))               #When you change any of the previous variable, it will change the value and ID

print("var3 is now changed")
print("printing id of var2 = ",id(var2))
print("printing id of var3 = ",id(var3))
print("printing id of var4 = ",id(var4))

a,b,c=5,'dexter',-10-4j         #You can assign multiple variables in one line,
print("a=",a)                   #Variables will be assigned in the order specified
print("b=",b)
print("c=",c)


#unpacking
OurString='Learn'
a,b,c,d,e=OurString  #if the variable count do not match, it will result in an error

print(a,b,c,d,e)

#To solve the issues with unpacking we use slicing
 



