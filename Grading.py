
marks1 = int(input("Marks 1: "))
marks2 = int(input("Marks 2: "))
grading_chart = {
    'A+': (90, 100),
    'A': (80, 89),
    'B': (70, 79),
    'C': (60, 69),
    'D': (50, 59),
    'F': (0, 49)
}
grade1 = None
grade2 = None
for grade, (lower, upper) in grading_chart.items():
    if lower <= marks1 <= upper:
        grade1 = grade
    if lower <= marks2 <= upper:
        grade2 = grade
if grade1 == grade2:
    print("Same Grades")
else:
    print("Different Grades")

