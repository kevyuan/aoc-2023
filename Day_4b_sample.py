import re

with open('Day_4_sample.txt') as f:
    cards = f.read().splitlines()

# for line in input:
#     schematic_array[row_number] = [char for char in line]
#     row_number += 1

cards_with_matches = []
points_list = []
result_list = []
wnp_begin = 2
wnp_end = 7
nyhp_begin = 8
nyhp_end = 16
number_of_cards = len(cards)

# Debug
# print(test_string)

# sample input
# Card   1: 81  1 43 40 49 51 38 65 36  4 | 21 15  1 43 60  9 83 81 35 49 40 38 82 65 20  4 58 94 16 89 84 10 77 48 76
# winning numbers are in positions 2 to 11
# numbers you have are in positions 13 to 37

# Process the list to find the number of matching numbers

for card in cards:

    # Reset points
    matches = 0
    card_array = card.replace(':', '').split()
    card_number = int(card_array[1])

    for winning_number_position in range(wnp_begin, wnp_end):
        for numbers_you_have_position in range(nyhp_begin, nyhp_end):
            if card_array[winning_number_position] == card_array[numbers_you_have_position]:
                matches += 1
    
    # How many matches am I allowed to have? 
    while (card_number + matches > number_of_cards):
        matches -= 1

    # Append to the new list using card with number of matches
    cards_with_matches.append(card.replace(':', '') + " " + str(matches))

# Debug
# print(cards_with_matches)


work_list = cards_with_matches.copy()
current_position = 0
count = 0

while (len(work_list) > 0):

    card = work_list.pop(0)
    card_array = card.replace(':', '').split()

    matches = int(card_array[nyhp_end])
    print(card)

    if matches == 0:
        pass
    else:
        for x in range (0, matches):
            work_list.append(cards_with_matches[int(card_array[1]) + x])

    count += 1

print(count)

# Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
# Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
# Your copy of card 2 also wins one copy each of cards 3 and 4.
# Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
# Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
# Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
# Your one instance of card 6 (one original) has no matching numbers and wins no more cards.


