def checkPalindrome(arr):
    if arr == arr[::-1]:
        print('YES')
    else:
        print('NO')


n = int(input())  
arr = list(map(int, input().split()))
checkPalindrome(arr)

