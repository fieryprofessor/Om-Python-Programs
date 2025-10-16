marks = float(input("Enter your marks: "))

if 90 <= marks <= 100:
    grade, comment = 'A', 'Excellent'
elif 80 <= marks < 90:
    grade, comment = 'B', 'Good'
elif 70 <= marks < 80:
    grade, comment = 'C', 'Average'
elif 60 <= marks < 70:
    grade, comment = 'D', 'Needs Improvement'
else:
    grade, comment = 'F', 'Failing'

print(f"Grade: {grade}, Comment: {comment}")
