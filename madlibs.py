def formatGrade(grade):
    if grade == 'K' or grade == 'k':
        return "kindergarten"
    elif grade == '1':
        return "1st"
    elif grade == '2':
        return "2nd"
    elif grade == '3':
        return "3rd"
    else:
        return (grade + "th")


girl_name = input("A girl's name: ")
grade = input("Her grade(K-5): ")
school_name = input("Name of her elementary school: ")
brother_name = input("Her brother's name: ")
candy = input("Her favorite candy: ")
costume = input("A Halloween constume: ")
bad_food = input("A food that eating too much of will make you sick: ")
gross_thing = input("Something that would be gross to clean: ")
scary_pet = input("A scary kind of pet: ")
# This line looks different...
num_candy = int(input("A number greater than 20: "))

# Use the word many or much depending on whether the bad food is plural or singular
if bad_food[-1] == 's':  # if the bad food ends in an 's'
    bad_food_phrase = 'many ' + bad_food  # use the to word 'many' to describe it
else:
    bad_food_phrase = 'much ' + bad_food  # use the word 'much'

print(f'''

Once there was a girl named {girl_name} who was in {formatGrade(grade)} grade at {school_name}. It was Halloween night, she had just gotten home from school, and was getting ready to go trick-or-treating. This year she was going as a {costume}. She was almost ready to go when her dad told her "I have some bad news, {brother_name} is sick from eating too {bad_food_phrase}, so he can\'t go tonight. But if you share your candy with him, you won\'t have to clean the {gross_thing} this weekend." {girl_name} was bummed, but she went trick-or-treating anyway and had a great time. She even visited her scary neighbors with the pet {scary_pet} that ran free in the yard. In total she brought home {num_candy} pieces of candy.

''')

if num_candy % 2 == 0:  # even number, will split evenly
    print(
        f'She was feeling generous so she split her candy evenly with {brother_name}, and they each got {num_candy//2} pieces.')
else:  # odd number, there will be 1 left over
    print(
        f'They each got {num_candy//2} pieces of candy, but there was 1 left over. While they were deciding how to split it,')
    print(f'her dad swooped by and took it for himself. "Happy Halloween!" he said, and smiled at them with a mouth full of chocolate.')
