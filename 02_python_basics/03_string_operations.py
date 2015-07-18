# Examples of Python strings:
print(
    "A simple string"
)
print(
    'There are no strings on me'
)
print(
    '"Of course" said noone in particular'
)
print(
    "Here's a string"
)
print(
    '"Here\'s a string" said the previous line'
)

some_html = """
<html>
<head>
<title>Some HTML in a Python string</title>
<body>
"We can use the quotation characters in here without issues," the author exclaimed.
Even this one: '
</body>
</html>
"""

print(some_html)

print(
    "You should never " + "ever " * 3 + "divide strings"
)

a_string = "FastTrack"
print(a_string[0])      # F
print(a_string[0:4])    # Fast
print(a_string[:4])     # Fast
print(a_string[4:])     # Track
print(a_string[-1])     # k
print(a_string[::2])    # FsTak
print(a_string[::-1])   # kcarTtsaF

print(
    'My name is {} and I am {} years old'.format('Mira Talwar', 32)
)
print(
    'My name is {name} and I am {age} years old'.format(name='Sujay Pillay', age=14)
)
