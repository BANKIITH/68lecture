student = {}  # สร้าง dictionary ว่าง

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))
student["score"] = int(input("Enter score: "))

print(f"ชื่อนักเรียน: {student['name']}, อายุ: {student['age']}, คะแนน: {student['score']}")
