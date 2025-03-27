def checkLucky(number):
    num = str(number)
    isLucky = True
    if '1' in num or '2' in num or '3' in num or '5' in num or '6' in num or '8' in num or '9' in num or '0' in num:
        isLucky = False
    return isLucky


a, b = map(int, input().split())

luckyNumbers = [str(i) for i in range(a, b + 1) if checkLucky(i)]

print(" ".join(luckyNumbers) if luckyNumbers else -1)  # Efficient output
