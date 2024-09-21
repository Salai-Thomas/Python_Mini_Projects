numbers_of_subject = int(input("Enter Numbers Of Subject: "))
pass_marks = int(input("Enter Pass Marks: "))
marks = []
all_passed = True

for subject in range(numbers_of_subject):
    mark = int(input("Enter marks for subject "+str(subject)+" : "))
    marks.append(mark)

for mark in marks:
    all_passed = all_passed and mark >= pass_marks

if all_passed:
    print("Pass")
else:
    print("Fail")
