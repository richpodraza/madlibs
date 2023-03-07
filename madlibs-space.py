year = input("A year: ")
job = input("A kind of job: ")
name1 = input("A person's name: ")
name2 = input("Another person's name: ")
vehicle = input("A kind of vehicle: ")
vehicle_name = input("A name for that vehicle: ")
space_junk = input("A type of space junk: ")
something_soft = input("Something very soft: ")
moon_thing = input("Something you might find on the moon: ")
alien = input("Type of alien: ")
greeting = input("A way to greet someone: ")
sport = input("A game or sport: ")

if something_soft[0:2] == 'a ' or something_soft[0:3] == 'an ':
    something_soft = something_soft
elif something_soft[0] in 'aeiou':
    something_soft = 'an ' + something_soft
else:
    something_soft = 'a ' + something_soft

print(f'''

In the year {year}, NASA sent a team of {job}s to visit the moon. This team was led by Neal Armstrong and his friends {name1} and {name2}. There was a countdown, and then they took off in a {vehicle} named {vehicle_name}. On the way to the moon, they saw {space_junk}s out the windows. The landing was as soft as {something_soft}. After they landed, they went for a moon walk. While they were collecting samples of {moon_thing}, they saw a {alien} appear in front of them! It said, "{greeting}, Earthlings." Then they all played a round of {sport}. The Earthlings won, so they piled back in their {vehicle} and went home to Earth.

''')
