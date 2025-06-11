# students_grade_analyzer.py

def display_student_summary(names, grades):
    print("\nStudent Summary:")
    print("----------------")
    for name, grade in zip(names, grades):
        print(f"{name}: {grade}")

def get_avg_grade(grades):
    return sum(grades) / len(grades) if grades else 0

def get_highest_grade(names, grades):
    highest = max(grades)
    index = grades.index(highest)
    return names[index], highest

def count_passed(grades):
    return sum(1 for grade in grades if grade >= 60)

def main():
    names = []
    grades = []

    try:
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            name = input(f"Enter name of student {i+1}: ")
            while True:
                try:
                    grade = float(input(f"Enter grade for {name} (0 - 100): "))
                    if 0 <= grade <= 100:
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric grade.")
            names.append(name)
            grades.append(grade)
    except ValueError:
        print("Please enter a valid number of students.")
        return

    display_student_summary(names, grades)
    avg = get_avg_grade(grades)
    top_student, top_grade = get_highest_grade(names, grades)
    passed_count = count_passed(grades)

    print("\nClass Statistics:")
    print("-----------------")
    print(f"Average Grade: {avg:.2f}")
    print(f"Highest Grade: {top_student} with {top_grade}")
    print(f"Number of Students Passed (>=60): {passed_count}")

if __name__ == "__main__":
    main()
