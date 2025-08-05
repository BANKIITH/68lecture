performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72],
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85],
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66],
    }
}

from statistics import mean

# 1. Average score per employee
average_scores = {}
for dept, employees in performance_data.items():
    for emp, scores in employees.items():
        average_scores[emp] = mean(scores)

# 2. Top performer per department
top_performers = {}
for dept, employees in performance_data.items():
    best_emp = max(employees.items(), key=lambda item: mean(item[1]))
    top_performers[dept] = (best_emp[0], mean(best_emp[1]))

# 3. Department with highest average performance
dept_avg_scores = {}
for dept, employees in performance_data.items():
    all_scores = [score for scores in employees.values() for score in scores]
    dept_avg_scores[dept] = mean(all_scores)
top_department = max(dept_avg_scores.items(), key=lambda item: item[1])

# 4. Employees with continuous improvement (scores strictly increasing)
improving_employees = []
for dept, employees in performance_data.items():
    for emp, scores in employees.items():
        if all(earlier < later for earlier, later in zip(scores, scores[1:])):
            improving_employees.append(emp)

# 5. Summary report
print("Summary Report")
print("=======================")
print("1. Average score per employee:")
for emp, avg in average_scores.items():
    print(f"   {emp}: {avg:.2f}")

print("\n2. Top performer per department:")
for dept, (emp, avg) in top_performers.items():
    print(f"   {dept}: {emp} with average {avg:.2f}")

print(f"\n3. Department with highest average score: {top_department[0]} ({top_department[1]:.2f})")

print("\n4. Employees with continuous improvement:")
for emp in improving_employees:
    print(f"   {emp}")
