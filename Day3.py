# Array
array = input().split()
arr = [int(i) for i in array]
total=0
for i in arr:
    total += i
print(total)

#String

string=input()
str=string.lower()
vow=0
cons=0
vow_letter='aeiou'

for i in str:
    if i.isalpha():
        if i in vow_letter:
            vow+=1
        else:
            cons+=1
print(vow)
print(cons)