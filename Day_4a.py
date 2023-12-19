import re

with open('Day_4_input.txt') as f:
    input = f.read().splitlines()

points_list = []

# sample input
# Card   1: 81  1 43 40 49 51 38 65 36  4 | 21 15  1 43 60  9 83 81 35 49 40 38 82 65 20  4 58 94 16 89 84 10 77 48 76
# winning numbers are in positions 2 to 11
# numbers you have are in positions 13 to 37

for card in input:

    # Reset points
    points = 0
    has_first_match = False

    card_array = card.split()

    for winning_number_position in range(2, 12):
        for numbers_you_have_position in range(13, 38):
            if card_array[winning_number_position] == card_array[numbers_you_have_position]:

                if has_first_match == False: 
                    has_first_match = True    
                    points = 1
                else:
                    points *= 2

                # Debug
                # print(points)
            
    points_list.append(points)

print(sum(points_list))