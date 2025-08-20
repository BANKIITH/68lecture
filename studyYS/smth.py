from graphviz import Digraph

# สร้าง Context Diagram
dot = Digraph("ContextDiagram", format="png")
dot.attr(rankdir="LR", size="8")

# Node ของระบบหลัก
dot.node("System", "ระบบจัดการร้านค้าสหกรณ์", shape="rectangle", style="filled", fillcolor="lightblue")

# External Entities
entities = {
    "Customer": "ลูกค้าทั่วไป",
    "Member": "สมาชิก",
    "Staff": "พนักงานขาย",
    "Manager": "ผู้จัดการร้านค้า",
    "Supplier": "บริษัท ร่วมค้าส่ง จำกัด"
}

for key, label in entities.items():
    dot.node(key, label, shape="oval", style="filled", fillcolor="lightyellow")

# ความสัมพันธ์
# ลูกค้าทั่วไป
dot.edge("Customer", "System", "ข้อมูลการซื้อสินค้า")
dot.edge("System", "Customer", "ใบเสร็จรับเงิน")

# สมาชิก
dot.edge("Member", "System", "รหัสสมาชิก + ข้อมูลการซื้อสินค้า")
dot.edge("System", "Member", "ใบเสร็จ + บันทึกยอดซื้อ + จดหมายปันผล")

# พนักงานขาย
dot.edge("Staff", "System", "แบบฟอร์มสมัครสมาชิกใหม่ / ข้อมูลการขาย")
dot.edge("System", "Staff", "บัตรสมาชิก")

# ผู้จัดการร้านค้า
dot.edge("Manager", "System", "กำหนดอัตราปันผล / ตรวจสอบผลการขาย")
dot.edge("System", "Manager", "รายงานสรุปผลการขาย / แจ้งปันผล")

# บริษัทคู่ค้า (Supplier)
dot.edge("System", "Supplier", "ใบสั่งซื้อสินค้า")
dot.edge("Supplier", "System", "ใบส่งสินค้า + สินค้า")

# บันทึกไฟล์
file_path = "/mnt/data/context_diagram.png"
dot.render(file_path, cleanup=True)
file_path
