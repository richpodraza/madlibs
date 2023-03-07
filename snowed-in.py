import textwrap

pet_name = input("Pet's name: ")
length_of_time = input("Length of time: ")
noun1 = input("Noun: ")
location = input("Location: ")
noun2 = input("Noun: ")
treasured_possession = input("Treasured possession: ")
plural_noun1 = input("Plural noun: ")
past_tense_verb1 = input("Past-tense verb: ")
part_of_a_house = input("Part of a house: ")
past_tense_verb2 = input("Past-tense verb: ")
plural_noun2 = input("Plural noun: ")
food = input("Type of food, plural: ")
adjective1 = input("Adjective: ")
past_tense_verb3 = input("Past-tense verb: ")
ing_verb = input("Verb ending in '-ing': ")
adjective2 = input("Adjective: ")
noun3 = input("Noun: ")


text = f'''

My dad and I drove with our dog {pet_name} for {length_of_time} until we reached a {noun1} cabin in the middle of the {location}. Nothing was around for miles except {noun2}! How would I survive without my {treasured_possession}? As soon as we arrived, a blizzard of {plural_noun1} started falling from the sky. Five hours later the storm had {past_tense_verb1} our cabin up to the windows. We couldn’t even open the {part_of_a_house}. “Now what?” I said. My dad {past_tense_verb2} and started to pile {plural_noun2} into the fireplace. That night we roasted {food} over the fire and told {adjective1} stories until the dog and I fell asleep. The next afternoon the roads were finally clear. So we {past_tense_verb3} back to the city. {ing_verb} at the cabin had been so tall that we decided to make the trip a family tradition. But next time I’ll bring a {noun3} just in case.

'''

print(textwrap.fill(text, 80))
