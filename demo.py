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

#Find the pair whose sum is target
next_list = [0,1,2,3,4,3,5,6,7,5,7,2,9,1]
target = int(input("Enter the target number:  "))
sec_list = []
for m in range(len(next_list)):
    for n in range(m):
        if next_list[m] + next_list[n] == target:
            sec_list.append([next_list[m], next_list[n]])
print(sec_list)