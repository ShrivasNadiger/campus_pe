

try:
    marks = []
    
    # Taking marks input for 5 subjects
    for i in range(1, 6):
        subject_mark = float(input(f"Enter marks for Subject {i} (out of 100): "))
        
        if subject_mark < 0 or subject_mark > 100:
            print("Marks should be between 0 and 100.")
            exit()
        
        marks.append(subject_mark)

    total = sum(marks)
    percentage = total / 5

    # Grade Calculation
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    # Pass/Fail condition
    result = "Pass" if all(m >= 40 for m in marks) else "Fail"

    print("\n=== RESULT ===")
    print("Marks:", marks)
    print("Total:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numeric marks.")