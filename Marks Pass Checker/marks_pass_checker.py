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

for subject in range(1,numbers_of_subject+1):
    mark = int(input("Enter marks for subject "+str(subject)+" : "))
    if mark < 40:
        all_passed = False

if all_passed:
    print("Pass")
else:
    print("Fail")
