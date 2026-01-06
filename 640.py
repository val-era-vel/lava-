def sum_three(a, b, c):
    if a == b or a == c or b == c:
        return 0
    else:
        return a + b + c
numbers = list(map(int, input().split()))
print(sum_three(numbers[0], numbers[1], numbers[2]))

