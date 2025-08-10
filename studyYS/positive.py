def positive_number() -> None:
    if num <= 0:
        return "number is negative"
    
    if num > 0:
        return "number is positive"
    
num = int(input("Enter a number: "))
print(positive_number())
