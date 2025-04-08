def minMaxIndex(arr):
    mn = 2000000
    minIndex = -1

    mx = -2000000
    maxIndex = -1

    for idx,val in enumerate(arr):
        if val < mn:
            mn = val
            minIndex = idx

        if val > mx:
            mx = val
            maxIndex = idx
    
    return minIndex, maxIndex


def main():
    n = int(input())  
    arr = list(map(int, input().split()))
    (minIndex, maxIndex) = minMaxIndex(arr)
    
    
    temp = arr[minIndex]
    arr[minIndex] = arr[maxIndex]
    arr[maxIndex] = temp

    print(*arr)

main()

