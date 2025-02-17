#3sum is 0
nums = [-1,0,1,2,-1,-4]
list = []
for a in range(len(nums)):
    for b in range(a):
        for c in range(b):
            if nums[a] + nums[b] + nums[c] == 0:
                list.append([nums[a],nums[b],nums[c]])
print(list)