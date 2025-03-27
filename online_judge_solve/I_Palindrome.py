number = int(input())
copyNum = number
reversedNum = ""

while number!=0:
    rem = number%10
    reversedNum += str(rem)
    number = int(number/10)
    
# convert to a number
convertedReversed = int(reversedNum)
print(convertedReversed)

# palindrome check
if convertedReversed == copyNum:
    print('YES')
else:
    print('NO')