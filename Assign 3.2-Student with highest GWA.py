# Programmed by: Rebekah Joy E. Sevial
# Problem 2 of Assignment 3
# Student with highest GWA

# Open text file that contains the name of the students with their GWA
with open("students_record.txt") as student_GWA:
# Initialize student name and their lowest possible GWA 
    highest_GWA = 5.00
    student_name = ""
# For loop to read each line of the text file
    for line in student_GWA:
# Function to split the name and GWA
        name, GWA_str = line.strip().split(" , ")
# If statement to get the name of student who got the highest GWA
        GWA = float(GWA_str)
        if GWA == highest_GWA:
            highest_GWA = GWA
            student_name = name
# Print the name of the student with highest GWA and thier GWA
print("Student with highest GWA: ", student_name)
print("Student's GWA: ", highest_GWA)