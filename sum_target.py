#Find the pair whose sum is target
next_list = [0,1,2,3,4,3,5,6,7,5,7,2,9,1]
target = int(input("Enter the target number:  "))
sec_list = []
for m in range(len(next_list)):
    for n in range(m):
        if next_list[m] + next_list[n] == target:
            sec_list.append([next_list[m], next_list[n]])
print(sec_list)