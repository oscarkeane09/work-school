#oscar

print("Hello. What is your name?")
name = input()

while True:
    grade = input("Enter your grade as a number: ")
    try:
        grade = int(grade)
        break
    except ValueError:
        print("Invalid. Use numbers only please.")



print(name, "has a grade of", grade)

student = [name, grade]

print(student[0].upper())

if student[1] >= 60:
    print("PASS")
else:
    print("FAIL")