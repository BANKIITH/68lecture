
print("""Please select operation
      1.Add
      2.Subtract
      3.Multiply
      4.Divide""")
#ถ้าเราทำสัญลักษณ์ """ จะสามารถเขียนได้หลายบรรทัด โดยไม่ต้องใช้คำสั่ง print ใหม่ 
choose = input("select 1,2,3,4: ")

#ตั้งชื่อตัวแปร เพื่อจะรับค่าที่ ผู้ใช้ จะใส่ 1 2 3 4

number1 = float(input("enter the first number: "))
number2 = float(input("enter the second number: "))

#โจทย์บอกให้เอาตัวเลข 2 ตัวมา + - * / จึงเกิดมาเป็น num 1 และ num 2

if choose == "1":    #ถ้าเราพิม 1 
    result = number1 + number2      
    print(f"result = {result} ")   
elif choose == "2":             #ถ้าเราพิม 2    
    result = number1 - number2      
    print(f"result = {result}")     
elif choose == "3":              #ถ้าเราพิม 3    
    result = number1 * number2      
    print(f"result = {result}")     
elif choose == "4":              #ถ้าเราพิม 4    
    result = number1 / number2      
    print(f"result = {result}")     #ปริ้น ผลลัพธ์ออกมาที่ได้จาก num1 num2
else:
    print("Wrong. only select 1,2,3,4") #กรณีตัวผู้ใช้ไม่ได้ใส่ เลข 1 2 3 4

#love you 3000
#รักหนิงนะครับรักเค้าคนนี้ไปนานๆเลยนะ

