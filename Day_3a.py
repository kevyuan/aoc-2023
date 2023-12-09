import re

def is_this_anything_but_a_digit_or_a_period(char):
    if (char.isnumeric() or char == '.'):
        return False
    else:
        return True

def do_we_keep_this(number_of_rows, number_of_columns, row_number, col_number, schematic_array):
    did_we_find_a_symbol = False    

    # If first row
    if (row_number == 0):
               
        # If first column
        if (col_number == 0):
            
            # print('-Debug-')
            # print('row_number')
            # print(row_number)
            # print('col_number')
            # print(col_number)

            # Check right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number+1])):
                did_we_find_a_symbol = True
                print('check right')

            # Check down
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number])):
                did_we_find_a_symbol = True            
                print('check down')

            # Check down-right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number+1])):
                did_we_find_a_symbol = True            
                print('check down-right')

        # If last column
        elif (col_number == number_of_columns-1):

            # Check left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number+1])):
                did_we_find_a_symbol = True
                print('check left')

            # Check down-left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number-1])):
                did_we_find_a_symbol = True
                print('check down-left')

            # Check down
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number])):
                did_we_find_a_symbol = True            
                print('check down')

        # If middle column
        else:

            # Check left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number-1])):
                did_we_find_a_symbol = True
                print('check left')

            # Check right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number+1])):
                did_we_find_a_symbol = True
                print('check right')

            # Check down-left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number-1])):
                did_we_find_a_symbol = True
                print('check down-left')

            # Check down
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number])):
                did_we_find_a_symbol = True            
                print('check down')

            # Check down-right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number+1])):
                did_we_find_a_symbol = True            
                print('check down-right')


    # If last row
    elif (row_number == number_of_rows-1):

        # If first column
        if (col_number == 0):
            
            # Check top
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number])):
                did_we_find_a_symbol = True            
                print('check top')

            # Check top-right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number+1])):
                did_we_find_a_symbol = True            
                print('check top-right')

            # Check right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number+1])):
                did_we_find_a_symbol = True
                print('check right')


        # If last column
        elif (col_number == number_of_columns-1):

            # Check top-left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number-1])):
                did_we_find_a_symbol = True
                print('check top-left')

            # Check top
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number])):
                did_we_find_a_symbol = True            
                print('check top')

            # Check left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number-1])):
                did_we_find_a_symbol = True
                print('check left')



        # If middle column
        else:

            # Check top-left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number-1])):
                did_we_find_a_symbol = True
                print('check top-left')

            # Check top
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number])):
                did_we_find_a_symbol = True            
                print('check top')

            # Check top-right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number+1])):
                did_we_find_a_symbol = True            
                print('check top-right')

            # Check left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number-1])):
                did_we_find_a_symbol = True
                print('check left')

            # Check right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number+1])):
                did_we_find_a_symbol = True
                print('check right')



    # If in between
    else:
        # If first column
        if (col_number == 0):
            # Check top
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number])):
                did_we_find_a_symbol = True            
                print('check top')

            # Check top-right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number+1])):
                did_we_find_a_symbol = True            
                print('check top-right')

            # Check right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number+1])):
                did_we_find_a_symbol = True
                print('check right')

            # Check down-left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number-1])):
                did_we_find_a_symbol = True
                print('check down-left')

            # Check down
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number])):
                did_we_find_a_symbol = True            
                print('check down')

        # If last column
        elif (col_number == number_of_columns-1):

            # Check top-left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number-1])):
                did_we_find_a_symbol = True
                print('check top-left')

            # Check top
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number])):
                did_we_find_a_symbol = True            
                print('check top')

            # Check left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number-1])):
                did_we_find_a_symbol = True
                print('check left')

            # Check down-left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number-1])):
                did_we_find_a_symbol = True
                print('check down-left')

            # Check down
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number])):
                did_we_find_a_symbol = True            
                print('check down')


        # If middle column
        else:

            # Check top-left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number-1])):
                did_we_find_a_symbol = True
                print('check top-left')

            # Check top
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number])):
                did_we_find_a_symbol = True            
                print('check top')

            # Check top-right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number-1][col_number+1])):
                did_we_find_a_symbol = True            
                print('check top-right')

            # Check left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number-1])):
                did_we_find_a_symbol = True
                print('check left')

            # Check right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number+1])):
                did_we_find_a_symbol = True
                print('check right')

            # Check down-left
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number-1])):
                did_we_find_a_symbol = True
                print('check down-left')

            # Check down
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number])):
                did_we_find_a_symbol = True            
                print('check down')

            # Check down-right
            if (is_this_anything_but_a_digit_or_a_period(schematic_array[row_number+1][col_number+1])):
                did_we_find_a_symbol = True            
                print('check down-right')


    return did_we_find_a_symbol


with open('Day_3_input.txt') as f:
    input = f.read().splitlines()

# Breakdown the schematic into a 2 dimensional array
schematic_array = {}
row_number = 0

for line in input:
    schematic_array[row_number] = [char for char in line]
    row_number += 1

    # Debug 
    # print(line)


# Get the number of rows and columns into a variable
number_of_rows = len(schematic_array)
number_of_columns = len(schematic_array[0])

# Debug
# print('number_of_rows')
# print(number_of_rows)
# print('number_of_columns')
# print(number_of_columns)




# Debug
# print(schematic_array[5][7])


is_this_a_keeper = False
row_number = 0
col_number = 0
part_number = ''
part_numbers = []




# Loop through each line

while row_number < number_of_rows:

    # print('-- Debug row number --')
    # print(row_number)
    col_number = 0

    # Traverse one character at a time
    while col_number < number_of_columns:

        # print('Debug')
        # print(row_number)
        # print(col_number)
        # print(schematic_array[row_number][col_number])
        # print(is_this_anything_but_a_digit_or_a_period(schematic_array[row_number][col_number]))    

        # If it is a number, append to the number string
        if schematic_array[row_number][col_number].isnumeric():
            part_number = part_number + schematic_array[row_number][col_number]

            # Debug
            # print('number_string')
            # print(part_number)

            # Scan surroundings to check whether we keep the number
            if(do_we_keep_this(number_of_rows, number_of_columns, row_number, col_number, schematic_array)):
                is_this_a_keeper = True

        # If it is not a number
        else:
            # print('-- Debug part_number --')
            # print(part_number)
            
            # If it is a keeper, append it to the list of numbers
            if(is_this_a_keeper):
                part_numbers.append(int(part_number))      

            # Reset the variables
            is_this_a_keeper = False
            part_number = ''

        # Increment the col
        col_number += 1

    # Increment the row
    row_number += 1






# Debug
print(part_numbers)
print(sum(part_numbers))



