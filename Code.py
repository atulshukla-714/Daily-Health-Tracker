calories = 0
water = 0  # in liters

print("==== Daily Health Tracker ====")

# Add calories
breakfast = int(input("Enter calories for breakfast: "))
lunch = int(input("Enter calories for lunch: "))
dinner = int(input("Enter calories for dinner: "))

calories = breakfast + lunch + dinner

# Add water intake
water = float(input("Enter total water intake today (in liters): "))

print("\n===== Today Summary =====")
print(f"Total Calories: {calories}")
print(f"Water Intake: {water} liters")