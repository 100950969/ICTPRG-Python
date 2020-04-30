grade = int(input('What was your grade: '))

if grade >= 90:
    print("You will receive a High Distinction")
elif grade >= 80:
    print("You will receive a Distinction")
elif grade >= 70:
    print("You will receive a Credit")
elif grade >= 50:
    print("You will receive a Pass")
elif grade <= 49:
    print("You have failed!!")