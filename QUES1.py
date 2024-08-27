input_string = input("Enter a string: ")

uppercase_chars = set()
lowercase_chars = set()


for char in input_string:
    if char.isupper():
        uppercase_chars.add(char)
    elif char.islower():
        lowercase_chars.add(char)


sorted_uppercase = sorted(uppercase_chars)
sorted_lowercase = sorted(lowercase_chars)


print("UPPERCASE:", ", ".join(sorted_uppercase))
print("Lowercase:", ", ".join(sorted_lowercase))
