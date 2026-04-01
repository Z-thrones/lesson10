medical_cause = input("Enter do you have a medical condition? Y for yes and N for no : ")
if medical_cause == "Y":
    print("You are alowwed to enter the exam")
else:
    atten = int(input("Please enter your attendance: "))
    if atten > 75:
        print("You are allowwed to enter the exam")
    else:
        print("You aren't allowwed to enter the exam")