nums = [45, 56, 76, 12, 43, 98]


# append(x)
nums.append(44)
print(nums)



# insert(i, x)
nums.insert(2, 33)
print(nums)



# remove(x)
if 56 in nums:
    nums.remove(56)
print(nums)



# pop()
last = nums.pop()
print(last, nums)




# index()
if 43 in nums:
    idx = nums.index(43)
    print(idx)





# sort()
nums.sort()
print(nums)





# reverse()
nums.reverse()
print(nums)