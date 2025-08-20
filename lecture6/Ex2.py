# สร้าง inventory
inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

# 1. ลดจำนวนสินค้า
def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            if item[1] < 0:
                item[1] = 0
            return
    print(f"{item_name} not found in inventory.")

# 2. คำนวณมูลค่ารวม
def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total += item[1] * item[2]
    return total

# 3. หาสินค้าราคาแพงที่สุด
def find_most_expensive(inventory):
    if not inventory:
        return None
    most_expensive = inventory[0]
    for item in inventory:
        if item[2] > most_expensive[2]:
            most_expensive = item
    return most_expensive[0]

# 4. เพิ่มหรืออัปเดตสินค้า
def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return
    inventory.append([item_name, quantity, price])

# ----------------------
# Actions ตามโจทย์
# 1. Update inventory หลังขาย 20 bananas
update_inventory(inventory, "Banana", 20)

# 2. คำนวณมูลค่ารวม
total_value = calculate_total_value(inventory)
print("Total inventory value: $", total_value)

# 3. หาสินค้าที่แพงที่สุด
expensive_item = find_most_expensive(inventory)
print("Most expensive item:", expensive_item)

# 4. Add Eggs และอัปเดต
add_item(inventory, "Eggs", 30, 0.25)
add_item(inventory, "Eggs", 50, 0.30)

print("Updated inventory:")
for item in inventory:
    print(item)
