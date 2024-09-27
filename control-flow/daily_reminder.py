# Prompt for a single task
task = input("Enter a task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = "Error: Invalid priority level. Please enter high, medium, or low."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This requires immediate attention today!"
elif time_bound == "no":
    reminder += " This is not time-sensitive."

# Output the customized reminder
print(reminder)
