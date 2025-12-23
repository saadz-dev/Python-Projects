activity = input("What activity did you do? ")
minutes = int(input("How many minutes did you do it for ? "))

print(f"Saved: {activity} - {minutes} minutes")

file = open("activity_log.txt", "a")
file.write(activity + " - " + str(minutes) + " minutes\n")
file.close()
