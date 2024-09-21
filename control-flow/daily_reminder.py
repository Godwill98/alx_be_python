#Prompt user for task description, priority, and whether it's time-bound
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Prepare base messages
error_message = "Something went wrong!"
first_part = f"{task} is a {priority} priority task"

# Use match-case for the task's priority
match priority:
    case "high":
        reminder = "that requires immediate attention today!"
    case "medium":
        reminder = "schedule it for later."
    case "low":
        reminder = "Consider completing it when you have free time."
    case _:
        reminder = error_message

# Modify the reminder based on whether the task is time-bound
if time_bound == "yes":
    reminder = "that requires immediate attention today!"
elif time_bound != "no":
    reminder = error_message  # Invalid input for time-bound

# Print the final reminder and message
print("Reminder:", reminder)
message = f"Reminder: '{task}' is a {priority} priority task. {reminder}"
print(message)
