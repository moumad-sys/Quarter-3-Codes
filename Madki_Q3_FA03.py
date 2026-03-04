1. Reused Dataset from Activity 1

I reused my Student Grade Tracker dataset, which contains quiz scores of 5 students in three subjects: Math, Science, and English.

2D Array:
grades = [
    [85, 90, 88],
    [78, 82, 80],
    [92, 89, 94],
    [70, 75, 72],
    [88, 91, 85]
]

Each row represents one student.
Each column represents a subject:

Column 0 → Math

Column 1 → Science

Column 2 → English

2. Summary Code (Total, Average, Highest)
# Print all student grades
print("Student Grades:")
for i in range(len(grades)):
    print("Student", i+1, ":", grades[i])

print("\nStudent Averages:")
# Calculate average per student
for i in range(len(grades)):
    total = sum(grades[i])
    average = total / len(grades[i])
    print("Student", i+1, "Average:", average)

# Calculate overall class average
all_scores = []
for row in grades:
    for score in row:
        all_scores.append(score)

overall_average = sum(all_scores) / len(all_scores)
print("\nOverall Class Average:", overall_average)

# Find highest score in the class
highest = max(all_scores)
print("Highest Score in Class:", highest)
3. Display of Output (Expected Output)

Student Grades:
Student 1 : [85, 90, 88]
Student 2 : [78, 82, 80]
Student 3 : [92, 89, 94]
Student 4 : [70, 75, 72]
Student 5 : [88, 91, 85]

Student 1 Average: 87.67
Student 2 Average: 80.00
Student 3 Average: 91.67
Student 4 Average: 72.33
Student 5 Average: 88.00

Overall Class Average: 83.93
Highest Score in Class: 94

4. Reflection on Summarizing

Using arrays made summarizing the dataset much easier and more organized. Because the data was stored in a 2D array, I was able to use loops to calculate totals, averages, and the highest score efficiently. Instead of writing separate variables for each student and subject, I accessed the values using indexing and iteration.

Arrays helped me analyze patterns in the class performance quickly. For example, I could compute each student’s average and also find the overall class average using built-in functions like sum() and max(). This shows how arrays are useful for handling grouped data in real-life situations such as grading systems and academic performance tracking.

Overall, this activity helped me understand how arrays are powerful tools for organizing and summarizing structured data accurately and efficiently.
