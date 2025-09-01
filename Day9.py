num = int(input())
power = len(str(num))
total = sum(int(digit) ** power for digit in str(num))

if num == total:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
