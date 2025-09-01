#numbers reverse
number=int(input())
rev = 0
n = number
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print(rev)

rev = int(str(number)[::-1])
print(rev)

#digit count
number=int(input())
sum=0
n = number
while n > 0:
    digit = n % 10
    sum+=1
    n //= 10
print(sum)
