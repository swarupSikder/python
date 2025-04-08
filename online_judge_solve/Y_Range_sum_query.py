def prefixSum(nums):
    arr = []
    arr.append(nums[0])
    sum = nums[0]

    for idx,num in enumerate(nums):
        if(idx==0):
            continue
        sum += num
        arr.append(sum)
    
    return arr
        

def main():
    [n,q] = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    preSum = prefixSum(nums)
    # print(preSum)
    
    while q:
        [l,r] = list(map(int, input().split()))
        if l==1:
            print(preSum[r-1])
        else:
            print(preSum[r-1] - preSum[l-2])
        q -= 1

main()