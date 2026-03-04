1. Dataset Idea (Clarity of Dataset Idea)

Title: Student Grade Tracker for 3 Subjects

My mini-dataset is about tracking students' quiz scores in three subjects: Math, Science, and English. This dataset is realistic because schools regularly record and compute student grades. It is useful for monitoring performance, identifying strengths and weaknesses, and computing averages.

The dataset will store quiz scores of 5 students. Each row represents one student, and each column represents a subject.

2. 2D Array Structure

Rows → Students
Columns → Subjects (Math, Science, English)

Student	Math	Science	English
Student 1	85	90	88
Student 2	78	82	80
Student 3	92	89	94
Student 4	70	75	72
Student 5	88	91	85
In array form:

grades = [ [85, 90, 88], [78, 82, 80], [92, 89, 94], [70, 75, 72], [88, 91, 85] ]

This structure is appropriate because:

Each row consistently represents one student.
Each column consistently represents one subject.
The data is organized clearly and is easy to access using row and column indices.
3. Sample Array Code

# 2D Array of student grades grades = [ [85, 90, 88], [78, 82, 80], [92, 89, 94], [70, 75, 72], [88, 91, 85] ] # Print all grades for row in grades: print(row)

4. Basic Array Operations

A. Print Operation

print("Student 1 Math grade:", grades[0][0])

B. Update Operation

(Change Student 4's Math grade from 70 to 75)

grades[3][0] = 75

C. Summarize Operation

(Compute the average grade of Student 3)

average = sum(grades[2]) / len(grades[2]) print("Student 3 Average:", average)

These operations show how we can access, modify, and summarize data using a 2D array.

5. Reflection and Explanation

I chose this dataset because grades are something students deal with regularly, making the example practical and easy to understand. Using a 2D array made the data more organized since each row represents a student and each column represents a subject. Instead of using separate variables for every score, the array keeps everything structured in one place.

Arrays help make calculations faster and easier. For example, we can quickly compute averages, update scores, or print all grades using loops. This shows how 2D arrays are useful in real-life situations such as school systems, grading software, and student performance tracking.

Overall, this project demonstrates how arrays help organize and manage structured data efficiently.
