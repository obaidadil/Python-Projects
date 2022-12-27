# Initialize the list of workouts
workouts = ["Pushups", "Squats", "Lunges", "Planks", "Burpees"]

# Initialize the dictionary to store the schedule
schedule = {}

# Welcome message
print("Welcome to the workout schedule app!")

# Prompt the user for the number of days in the schedule
num_days = int(input("How many days do you want in your schedule? "))

# Create the schedule
for i in range(num_days):
  day = input("Enter the name of day {}: ".format(i+1))
  workout = input("Enter the workout for {}: ".format(day))
  schedule[day] = workout

# Print the schedule
print("\nHere is your schedule:")
for day, workout in schedule.items():
  print("{}: {}".format(day, workout))
