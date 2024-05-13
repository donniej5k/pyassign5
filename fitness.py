# 5. The Fitness Tracker

#Objective:
#The aim of this assignment is to create a program that tracks fitness activities and calories burned.

#Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

#Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5

#Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

# Task 1
def log_activities(activities, durations):
    activity_log = dict(zip(activities, durations))
    return activity_log

# Task 2
def estimate_calories_burned(duration):
    return duration * 3.5  # Assuming a constant of 3.5 calories burned per minute

# Task 3
def generate_summary(activity_log):
    total_calories_burned = 0
    print("Fitness Activity Summary:")
    for activity, duration in activity_log.items():
        calories_burned = estimate_calories_burned(duration)
        total_calories_burned += calories_burned
        print(f"{activity}: {duration} minutes, Calories Burned: {calories_burned}")
    print("Total Calories Burned for the Day:", total_calories_burned)

# Main function
def main():
    activities = ['Dancing', 'Swimming', 'Biking']
    durations = [10, 20, 15]

    activity_log = log_activities(activities, durations)
    generate_summary(activity_log)

# Entry point of the program
if __name__ == "__main__":
    main()

