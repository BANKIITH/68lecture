score = int(input("Enter a test score: "))

while score < 0 or score > 100:
    print("ERROR: Stupid cannot be negative")
    print("or then 100")
    score = int(input("Enter a correct score: "))

print("the score is", score)