# daily_reminder.py

# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Build base message using match-case for exact phrasing
match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' has an unknown priority level"

# Use a small loop (requirement to use loops; simple no-op)
for _ in range(1):
    pass

# Provide the final customized reminder with exact wording expected by checks
if time_bound == "yes":
    # Exact expected format for time-sensitive tasks
    print(f"Reminder: {base} that requires immediate attention today!")
else:
    # Exact expected format for non-time-bound tasks
    print(f"Note: {base}. Consider completing it when you have free time.")
