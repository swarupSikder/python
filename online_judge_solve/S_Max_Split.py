def main():
    line = input()
    lineStream = []

    count_L = 0
    count_R = 0
    count_main = 0
    word = ""

    for ch in line:
        word += ch

        if ch=='L':
            count_L += 1

        if ch=='R':
            count_R += 1

        if count_L == count_R:
            count_main += 1
            count_L = 0
            count_R = 0
            lineStream.append(word)
            word = ""

    print(count_main)

    for w in lineStream:
        print(w)

main()