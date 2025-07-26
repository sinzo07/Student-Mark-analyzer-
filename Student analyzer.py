sub1 = int(input("Subject 1 mark: "))
sub2 = int(input("Subject 2 mark: "))
sub3 = int(input("Subject 3 mark: "))
sub4 = int(input("Subject 4 mark: "))
sub5 = int(input("Subject 5 mark: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5

print("\nTotal Marks:", total)
print("Average Marks:", average)
if sub1 >= 35 and sub2 >= 35 and sub3 >= 35 and sub4 >= 35 and sub5 >= 35:
    print("Result: Pass")
    
    if average >= 90:
        print("Grade: A+")
    elif average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Result: Fail")
    print("Grade: F")