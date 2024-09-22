def get_valid_input(prompt):
    while True:
        try:
            value = input(prompt)
            if value.isalpha():
                raise ValueError("Invalid Value.Value Must Be Number.")
            else:
                value = int(value)
                
            if value == 0:
                raise ValueError("Value Can't Be 0.Please Try Again.")
            return value
        except ValueError as e:
            print(e)

numbers_of_subject = get_valid_input("Enter Numbers Of Subject: ") 
pass_marks = int(input("Enter Pass Marks: "))
marks = []
all_passed = True

for subject in range(numbers_of_subject):
    mark = int(input("Enter marks for subject "+str(subject+1)+" : "))
    marks.append(mark)

for mark in marks:
    all_passed = all_passed and mark >= pass_marks

if all_passed:
    print("Pass")
else:
    print("Fail")
