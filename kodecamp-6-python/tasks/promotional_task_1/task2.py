# The Temperature Consultant

# Ask the user for the current temperature in Celsius.
# Logic:
# Above 30: "It's hot, stay hydrated!"
# 15 to 30: "Perfect weather."
# Below 15: "Wear a jacket."

temperature = float(input("Enter the current temperature in Celsius: "))

if temperature > 30:
    print("It's hot, stay hydrated!")
elif temperature >= 15:
    print("Perfect weather.")
else:
    print("Wear a jacket.")