input_string = input("Enter stiring: ")

modified_string = ""

vowels = "aeiouAEIOU"

for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
        modified_string += "*"
    else:modified_string += upper_char

print(f"modified string: {modified_string}")