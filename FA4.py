number_students = int(input("Enter number of students: "))
number_subjects = int(input("Enter number of subjects per student: "))

overall_total = 0  
overall_count = 0  

for student in range(1, number_students + 1):
    print(f"\nStudent {student}")
    students_total = 0

    for subject in range(1, number_subjects + 1):
        score = float(input(f"Enter score {subject}: "))
        students_total += score
        overall_total += score
        overall_count += 1

    student_average = students_total / number_subjects
    print(f"Average for Student {student}: {student_average:.2f}")

class_average = overall_total / overall_count
print(f"\nOverall Class Average: {class_average:.2f}")
