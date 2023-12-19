import re

with open('Day_4_sample.txt') as f:
    input = f.read().splitlines()

# for line in input:
#     schematic_array[row_number] = [char for char in line]
#     row_number += 1


points_list = []


test_string = input[0].split()

# Debug
# print(test_string)

# sample input
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# winning numbers are in positions 2, 3, 4, 5, 6
# numbers you have are in positions 8, 9, 10, 11, 12, 13, 14, 15

for card in input:

    # Reset points
    points = 0
    has_first_match = False

    card_array = card.split()

    for winning_number_position in range(2, 7):
        for numbers_you_have_position in range(8, 16):
            if card_array[winning_number_position] == card_array[numbers_you_have_position]:
                
                # if lock == True:
                #     lock = False
                # else:
                #     points *= 2 

                if has_first_match == False: 
                    has_first_match = True    
                    points = 1
                else:
                    points *= 2

                # Debug
                # print(points)
            
    points_list.append(points)

print(points_list)