# สร้าง dictionary ชื่อ phonebook
phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333', 'Pluto': '777-4444'}

# สร้าง dictionary เปล่าชื่อ heroesdict
heroesdict = {} 
# heroesdict = dict() ก็ใช้ได้เหมือนกัน

# เพิ่มข้อมูลลงใน heroesdict
heroesdict['Hulk'] = '888-1111'
heroesdict['Iron Man'] = '888-2222'

# ใช้ .get() เพื่อดึงค่าจาก key
# ถ้าหา key ไม่เจอ จะแสดงข้อความสำรอง
print(heroesdict.get('Halk', 'Key not found'))  
# ผลลัพธ์: Key not found
print(heroesdict.get('Hulk', 'Key not found'))
# ผลลัพธ์: 888-1111

# วนลูปเพื่อแสดงข้อมูลใน phonebook
for key, value in phonebook.items():
    print(key, value)
# ผลลัพธ์:
# Anirach 777-1111
# Mickey 777-2222
# Donald 777-3333
# Pluto 777-4444

# แสดงผลลัพธ์ที่เป็นมุมมองของ key ทั้งหมด
print(phonebook.keys())
# ผลลัพธ์: dict_keys(['Anirach', 'Mickey', 'Donald', 'Pluto'])

# แสดงผลลัพธ์ที่เป็นมุมมองของ value ทั้งหมด
print(phonebook.values())
# ผลลัพธ์: dict_values(['777-1111', '777-2222', '777-3333', '777-4444'])

# ใช้ .pop() เพื่อลบข้อมูลด้วย key และรับค่าที่ถูกลบ
# ถ้าหา key ไม่เจอ จะแสดงข้อความสำรอง
print(phonebook.pop('Mick', 'Element not found'))
# ผลลัพธ์: Element not found

# ลบคู่ key-value ของ 'Mickey'
print(phonebook.pop('Mickey', 'Element not found'))
# ผลลัพธ์: 777-2222

# แสดง phonebook ที่เหลืออยู่
print(phonebook)
# ผลลัพธ์: {'Anirach': '777-1111', 'Donald': '777-3333', 'Pluto': '777-4444'}

# ใช้ .popitem() เพื่อลบคู่ key-value คู่สุดท้ายออก
print(phonebook.popitem())
# ผลลัพธ์: ('Pluto', '777-4444')

# แสดง phonebook ที่เหลืออยู่
print(phonebook)
# ผลลัพธ์: {'Anirach': '777-1111', 'Donald': '777-3333'}

# ใช้ .clear() เพื่อลบข้อมูลทั้งหมดใน dictionary
phonebook.clear()
print('After clear')
print(phonebook)
# ผลลัพธ์:
# After clear
# {}