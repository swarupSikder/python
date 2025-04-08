from collections import Counter

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    # edge case
    if n == 1:
        if nums[0] == 1:
            print(0)  #1 appears once, already a good sequence
        else:
            print(1)  #any other number should be removed
        return

    # freq = [0]*100005
    freq = Counter(nums)
    # print(freq)

    #main calculation
    count = 0
    for num, cnt in freq.items():
        if cnt < num:
            count += cnt  #remove all cnt
        else:
            count += cnt - num  #remove extra cnt

    print(count)
                
main()