student_name = "Bryce Bellerand"
current_gpa = 3.2 #float betweeen 1.0 - 4.0
study_hours = int(5) #integer
social_points = int(32)
stress_level = 75 #integer 1-100
passing = None
light_classes = ["Programming", "Calculus", "English"]
medium_classes = ["Programming", "Calculus", "English", "Colliquim"]
heavy_classes = ["Programming", "Calculus", "English", "Colliquim", "Engineering"]
#Display welcome stats

print(f"Welcome, {student_name}!")
print(f"GPA: {current_gpa}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")

print("Choose your course load:")
print("A) Simple (12 credits), perfect for a low stress!")  
print("B) Standard (15 credits) perfect middle ground of busy and free time")
print("C) Difficult (18 credits) if you don't like having time on your hands")
choice = input("Your choice: ")
if choice == "A":    # Use comparison operators to check GPA and adjust variables
    print(f"Good choice! Your classes are: {light_classes}")
    study_hours = len(light_classes) * 4
elif choice == "B":    # Different logic path
    print(f"Good choice! Your classes are: {medium_classes}")
    study_hours = len(medium_classes) * 4
elif choice == "C":    # Heavy load - check if GPA >= 3.5 for different outcomes
    if current_gpa >= 3.5:
        print(f"A more difficult set up but I know you can do it! Your classes are: {heavy_classes}")
        study_hours = len(heavy_classes) * 6
    else:
        print(f"I don't know if you're ready for that... I'll set you up with the standard classes for now. Your classes are: {medium_classes}")
else:
    print(f"Since you wanna be a lazy nigga, I guess I'll be giving you the simple set up. Your classes are: {light_classes}")
    study_hours = len(light_classes) * 4
