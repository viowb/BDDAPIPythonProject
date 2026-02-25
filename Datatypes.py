#Numeric
#list can be redeclared, modified and updated []
values = [1, 2, "Santander", 78, 9, 16, 89, 5, 4]
print(values[0])
print(values[2])
print(values[-1])  #to print the last index in a long list
print(values[-2])
print(values)
print(values[0:5])
#to insert additional values into an existing list use .insert
values.insert(3, 12)
print(values)
#dd a new variable to end
values.append("Ending")
print(values)
values.remove("Santander")
print(values)
#update index 2 value
values[2]= "API"
print(values)

#Tuple immutable, cant be updated once declared ()
val = (1,2,"test", 3.9) #this is a tuple
print(val)
print(val)

#Dictionary {}
dict = {1:"ring", "aim": "viowb", "age":63, 15 : 78}
print(dict)
print(dict["aim"])
print(dict["age"])
print(dict[5])
print(dict[1])


#you cannot concartinate diff data types it will give errors. use format

#Integer


#String


#Float
