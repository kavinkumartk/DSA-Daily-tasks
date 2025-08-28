#Pass by Value
def modify_number(a):
    print("Inside function, before change:", a)
    a = a + 10
    print("Inside function, after change:", a)
x = 5
print("Before function call:", x)
modify_number(x)
print("After function call:", x) 

#Pass by Reference

def modify_list(lst):
    print("Inside function, before change:", lst)
    lst.append(4)
    print("Inside function, after change:", lst)

my_list = [1, 2, 3]
print("Before function call:", my_list)
modify_list(my_list)
print("After function call:", my_list) 