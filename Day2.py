
#If/else statement
marks=int(input())
if marks>=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=50:
    print("Grade C")
elif marks>=35 :
    print("Grade D")
else:
    print("Fail")
    
#Switch Case

day = int(input("Enter a number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")
