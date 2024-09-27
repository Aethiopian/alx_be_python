import os

# Check if the script file exists and is not empty
if not os.path.exists(__file__) or os.path.getsize(__file__) == 0:
    print("Error: The script file does not exist or is empty.")
    exit()

# Prompt for a single task
task = input("Enter your task: ").strip()
if not task:
    print("Error: Task description cannot be empty.")
    exit()

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower().strip()
if priority not in ['high', 'medium', 'low']:
    print("Error: Invalid priority level. Please enter high, medium, or low.")
    exit()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
if time_bound not in ['yes', 'no']:
    print("Error: Please answer with 'yes' or 'no'.")
    exit()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = "Error: Invalid priority level."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This requires immediate attention today!"
elif time_bound == "no":
    reminder += " This is not time-sensitive."

# Output the customized reminder
print(reminder)
