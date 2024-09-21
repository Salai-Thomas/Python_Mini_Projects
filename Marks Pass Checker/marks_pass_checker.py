def get_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid Value Please Type Number")

numbers_of_subject = get_valid_input("Enter Numbers Of Subject: ") 
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
