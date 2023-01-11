# nums = [2,7,11,32]
# target = 39

nums = [3,2,4]
target = 6
for a in range(0,len(nums)):
    for b in range(a+1,len(nums)):
        if nums[a]+nums[b] == target :
            print([a,b])
            break
        
# a + b = target
# a = target - b

# if we have one value given then we can find another value as well
for b in range(0,len(nums)):
    a = target - nums[b]
    if a in nums and b!=nums.index(a):
        print([b,nums.index(a)])
        break