# task 1
import re

pattern = r'^ab*$'  
text = input("Enter string: ")
print(bool(re.match(pattern, text)))

# task 2
pattern = r'^ab{2,3}$'  # 'a' followed by 2 to 3 'b's
text = input("Enter string: ")
print(bool(re.match(pattern, text)))

# task 3
pattern = r'\b[a-z]+_[a-z]+\b'  
text = input("Enter string: ")
print(re.findall(pattern, text))

# task 4
pattern = r'\b[A-Z][a-z]+\b'
text = input("Enter string: ")
print(re.findall(pattern, text))

# task 5
pattern = r'^a.*b$'
text = input("Enter string: ")
print(bool(re.match(pattern, text)))

# task 6
pattern = r'[ ,.]'
text = input("Enter string: ")
print(re.sub(pattern, ":", text))

# task 7
def snake_to_camel(s):
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

text = input("Enter snake_case string: ")
print(snake_to_camel(text))

# task 8
pattern = r'(?=[A-Z])'
text = input("Enter string: ")
print(re.split(pattern, text))

# task 9
pattern = r'([a-z])([A-Z])'
text = input("Enter string: ")
print(re.sub(pattern, r'\1 \2', text))

# task 10
def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

text = input("Enter CamelCase string: ")
print(camel_to_snake(text))
