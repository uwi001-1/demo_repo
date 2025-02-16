#KRIPA Triangle
name = "KRIPA"
for i in range(len(name)):
    nam = name[0:i+1:1]
    print(nam)

#3sum is 0
nums = [-1,0,1,2,-1,-4]
list = []
for a in range(len(nums)):
    for b in range(a):
        for c in range(b):
            if nums[a] + nums[b] + nums[c] == 0:
                list.append([nums[a],nums[b],nums[c]])
print(list)

#Factorial recursive
def factorial(n):
    if n == 1:
        return n
    return n* factorial(n-1)
print(factorial(7))

# Fibonnaci Series 1 1 2 3 5 8 13 21
def fibonnaci():
    x= 1
    y= 1 
    for i in range(10):
        print(x)
        # z = x + y
        # x = y
        # y = z
        x,y = y, x+y
fibonnaci()

my_list = []
x= 1
y= 1 
for i in range(10):
    my_list.append(x)
    x,y = y, x+y
print(my_list)

#Find the pair whose sum is target
next_list = [0,1,2,3,4,3,5,6,7,5,7,2,9,1]
target = int(input("Enter the target number:  "))
sec_list = []
for m in range(len(next_list)):
    for n in range(m):
        if next_list[m] + next_list[n] == target:
            sec_list.append([next_list[m], next_list[n]])
print(sec_list)

#Plaindrome
s = input("Enter a string to check for palindrome:  ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")