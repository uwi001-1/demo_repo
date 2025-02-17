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