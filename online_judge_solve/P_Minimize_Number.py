def allEven(nums):
    flag = True
    for num in nums:
        if num%2==1:
            flag = False
    return flag
    
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    
    count = 0
    while allEven(nums):
        nums = [int(x/2) for x in nums if allEven(nums)]
        count += 1
 
    # print(nums)
    print(count)

main()