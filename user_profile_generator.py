# User Profile Generator

first = input("First name: ")
last = input("Last name: ")
age = input("Age: ")
city = input("City: ")
job = input("Occupation: ")

# full name using concatenation
full_name = first + " " + last

# sentence using formatting
info = f"You are {age} years old and you live in {city}. Your job is {job}."

# escape characters
profile = "Your profile:\n\"" + info + "\""

# string methods
full_name_upper = full_name.upper()

if job.startswith(("a", "e", "i", "o", "u")):
    profile = profile.replace(" a ", " an ")

print("\n--- USER PROFILE ---")
print("Name:", full_name_upper)
print(profile)
