## Task1## -
Name = input("Enter your name: " )
age = int(input("Enter your age: "))
Height= float(input("Enter your height in meters: "))
Is_Student =input("Enter Are you student or not (True/false): ").strip().lower()
print("\nEntered Details:")
print(Name, age, Height, Is_Student)
## Task 2##-- String Format
print(f"\nNAME:{Name}|AGE:{age}|HEIGHT: {Height}|IS_STUDENT:{Is_Student}")
## Task 3--Arithmetic Operations  ##
age_in_months = age * 12
age_in_days = age * 365
remainder = age % 7
age_squared = age ** 2

print("\nAge Calculations:")
print(f"Age in months: {age_in_months}")
print(f"Age in days: {age_in_days}")
print(f"Remainder when age is divided by 7: {remainder}")
print(f"Age squared: {age_squared}")
