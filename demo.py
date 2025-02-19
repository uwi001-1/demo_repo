#KRIPA Triangle
name = "KRIPA"
for i in range(len(name)):
    nam = name[0:i+1:1]
    print(nam)

#Factorial recursive
def factorial(n):
    if n == 1:
        return n
    return n* factorial(n-1)
print(factorial(7))