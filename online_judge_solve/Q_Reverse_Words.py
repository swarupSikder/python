def main():
    lineStream = input().split(' ')
    
    # print(lineStream)
    line = []

    for word in lineStream:
        revWord = word[::-1]
        line.append(revWord)

    print(*line)

main()