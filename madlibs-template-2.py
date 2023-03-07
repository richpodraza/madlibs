import textwrap

input1 = input("Input #1: ")
input2 = input("Input #2: ")

text = f'''

This is a story made with inputs {input1} and {input2}

'''

print(textwrap.fill(text, 80))
