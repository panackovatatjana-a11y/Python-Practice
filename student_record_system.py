# Student Record Management System

# --- Tuples ---
students = (
    ("Emmanuel", 20, "A"),
    ("Square", 19, "B"),
)

print("Students:", students)
print("Number of students:", len(students))
print("Index of Square:", students.index(("Square", 19, "B")))

# --- Sets ---
student_ids = {101, 102, 103}
courses = {"Math", "Physics", "Biology"}

print("Student IDs:", student_ids)
print("Courses:", courses)

# Set operations
student_ids.update({104})
print("Updated IDs:", student_ids)

completed = {"Math"}
print("Remaining courses:", courses - completed)
print("All courses:", courses.union({"Chemistry"}))

# --- Frozen Sets ---
frozen_students = frozenset(students)
frozen_courses = frozenset(courses)

print("Frozen students:", frozen_students)
print("Frozen courses:", frozen_courses)
