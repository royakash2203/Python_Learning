
print("hello")
var1 = "i am roy "
var2 = 8
var3 = 23.9
var4 = "good boy"
var5 = "12"
var6 = "36"
print(var1)
print(type(var3))
print(var2+var3)
#print(var1+var2)    #wrong
print(var1+var4)
#print(var5+var6)     #wrong
print(int(var5)+int(var6))
print(10*"akash\n")
#print(10*int(var5)+int(var6))    #wrong
#print(10 * "int(var5)+int(var6)")    #wrong
print(10 * str(int(var5)+int(var6)))

print("enter your number")
number1 = input()
print("you entered", number1)
#print("you entered", number1+10)    #wrong
print("your answer", int(number1)+10)

print("enter 1st number")
num1 = input()
print("enter 2nd number")
num2 = input()
print("answer", int(num1)+int(num2))
"""
str()
int()
float()
"""