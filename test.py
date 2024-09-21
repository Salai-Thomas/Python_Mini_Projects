numbers_of_subject = int(input("Enter Numbers Of Subject: "))
pass_marks = int(input("Enter Pass Marks: "))
marks = []
isPass = True

for subject in range(numbers_of_subject):
    mark = int(input("Enter marks for subject"+str(subject)+":"))
    marks.append(mark)

for mark in marks:
    isPass = isPass and mark >= 40

if isPass:
    print("Pass")
else:
    print("Fail")
