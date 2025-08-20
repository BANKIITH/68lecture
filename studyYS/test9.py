name = input("Enter name: ")
age = input("Enter age: ")

with open("student.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

print("บันทึกข้อมูลเรียบร้อยแล้วใน student.txt")
