# Student Grade Calculator (Very Simple)

scores = [78, 85, 92, 67, 88]

# Calculate average
average = sum(scores) // len(scores)

# Calculate grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Add "+" if needed
if average % 10 >= 5:
    grade += "+"

# Extra calculations
score_exists = 85 in scores
same_object = scores is scores
bitwise_and = scores[0] & scores[1]

print("=== Student Grade Calculator ===")
print("Scores:", scores)
print("Average:", average)
print("Grade:", grade)
print("Is 85 in scores?", score_exists)
print("Bitwise AND of first two scores:", bitwise_and)
