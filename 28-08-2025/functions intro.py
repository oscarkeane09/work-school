def square(n): #squares a number
    return n * n


def is_even(num):       #check if a number is even
    if num % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"
    
def string_length(st):
    return len(st)

print(square(20))
print(is_even(12))
print(string_length("test"))