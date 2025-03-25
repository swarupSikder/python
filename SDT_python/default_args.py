def sum(num1, num2, num3=0):
    result = num1 + num2
    return result

total = sum(99, 11)
print('total: ', total)

# args (tuple => building an array like object)
def all_sum(num1, num2, *nums):
    print(nums)
    sum = 0
    for num in nums:
        print(num)
        sum += num
    return sum

total = all_sum(45, 55, 67, 34, 12)
print('all-sum: ', total)