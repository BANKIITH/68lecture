scores = []
for i in range(5):
    score = int(input("Enter a score: "))
    scores.append(score)

average = sum(scores) / len(scores)


if average >= 50:
    print("ผ่าน")
else:
    print("ไม่ผ่าน")

print("คะแนนที่กรอก:", scores)
print("ค่าเฉลี่ย =", average)