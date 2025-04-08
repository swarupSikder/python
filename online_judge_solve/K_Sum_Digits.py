def k_sum_digits(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

n = int(input())
arr = list(map(int, input()))
print(k_sum_digits(arr))