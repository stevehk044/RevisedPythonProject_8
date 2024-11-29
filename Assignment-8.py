# Define the function to calculate the grade
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else: return 'F'

# Prompt the user to enter their marks for three subjects
marks1 = float(input("Enter your marks for subject 1: "))
marks2 = float(input("Enter your marks for subject 2: "))
marks3 = float(input("Enter your marks for subject 3: "))
# Calculate the average of the marks
average = (marks1 + marks2 + marks3) / 3
# Determine the grade based on the average
grade = calculate_grade(average)
# Display the calculated grade
print(f"Your average mark is: {average:.2f}")
print(f"Your grade is: {grade}")
