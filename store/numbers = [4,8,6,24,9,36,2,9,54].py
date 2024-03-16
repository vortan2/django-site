numbers = [4,8,6,24,9,36,2,9,54,84]
numbers_sum = 0
for number in numbers:
    if number % 6 == 0 and int(str(number)[-1]) == 4:
        numbers_sum += number
print(numbers_sum)
