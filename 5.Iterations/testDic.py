word_dict = {'a':
                {
                 'apple': 'the round fruit of a tree of the rose family',
                 'ant': 'an insect which cleans up the floor'
                },
             'b':
                {
                 'bad': 'of poor quaity or low standard',
                 'business': 'season 8 of GOT'
                }
            }

# Simple nexted for loop 
my_al_list = []

for letter, combo in word_dict.items():
    for meaning in combo.values():
        my_al_list.append(meaning)

print(f"The meanings in the dictionary are {my_al_list}")

print("")
my_al_list = [list(combo.values()) for index, combo in word_dict.items()]
print(f"Before flatte: {my_al_list}")

for meanings in my_al_list:
    for meaning in meanings:
        print(meaning)

final_list = [meaning for meanings in my_al_list for meaning in meanings]
print(f"final version using a list comprehension {final_list}")

# Using a itertolls chain + comprehension combo
from itertools import chain
my_chain = list(chain.from_iterable([list(combo.values()) for index, combo in word_dict.items()]))

print(f"final version using a chian {my_chain}")