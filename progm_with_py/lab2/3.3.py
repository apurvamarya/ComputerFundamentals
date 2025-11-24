print("Grade Calculator with Statistics")
print("-" * 40)

# Get number of tests

while True:
    try:
        num_tests = int(input("How many tests did you take? "))
        if num_tests > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")
        
# Collect test scores

scores = []
total = 0

for i in range(num_tests):
    while True:
        try:
            score = float(input(f"Enter score for test {i + 1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                total += score
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
            
# Calculate statistics

average = total / num_tests
highest = max(scores)
lowest = min(scores)

# Determine letter grade

if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
# Display results

print("\n" + "="*40)
print("GRADE REPORT")
print("="*40)
print(f"Number of tests: {num_tests}")
print(f"Test scores: {scores}")
print(f"Average score: {average:.1f}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Letter grade: {letter_grade}")

# Additional feedback

if letter_grade in ["A", "B"]:
    print("Excellent work! Keep it up!")
elif letter_grade == "C":
    print("Good job! There's room for improvement.")
else:
    print("You might want to study more for the next tests.")