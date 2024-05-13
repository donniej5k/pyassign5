# 3. The Grade Analyzer

#Objective:
The aim of this assignment is to analyze a set of grades and provide statistics.

#Task 1: Code a function to calculate the average grade.
#Task 2: Implement a function to find the highest and lowest grade.
#Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).


# Task 1 Function to calculate the average grade
def calculate_average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)

# Task 2 Function to find the highest and lowest grade
def find_highest_lowest(grades):
    if not grades:
        return None, None
    highest = max(grades)
    lowest = min(grades)
    return highest, lowest

# Task 3 Function to categorize grades into letter grades
def categorize_grades(grades):
    if not grades:
        return None
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')
    return letter_grades

# Main function
def main():
    grades = [75, 80, 92, 65, 88, 70]
    average = calculate_average(grades)
    highest, lowest = find_highest_lowest(grades)
    letter_grades = categorize_grades(grades)

    print("Statistics:")
    print("Average Grade:", average)
    print("Highest Grade:", highest)
    print("Lowest Grade:", lowest)
    print("Letter Grades:", letter_grades)

# Entry point of the program
if __name__ == "__main__":
    main()
