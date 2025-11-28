def calculate_speed(distance, time):
    if time == 0:
        return "Error: Time cannot be zero"
    return distance / time

# User input
distance = float(input("Enter distance (in kilometers): "))
time = float(input("Enter time (in seconds): "))

result = calculate_speed(distance, time)
print("Speed =", result)