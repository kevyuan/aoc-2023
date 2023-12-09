import re

with open('Day_2_input.txt') as f:
    games = f.read().splitlines()


red_limit = 12
green_limit = 13
blue_limit = 14

sum_of_ids = 0

for game in games:

    # Decompose the line
    game_number = re.search(r'Game \d+: ', game).group(0)
    id = int(re.search(r'\d+', game_number).group(0))

    # Debug
    print('--id: ' + str(id))

    # Remove the game number
    game = re.sub(r'Game \d+: ', '', game)

    # Create a list of sets
    sets = game.split(r';')

    # Initialize counters
    red = 0
    green = 0
    blue = 0 

    for set in sets:

        # Create a list of cube sets
        cube_sets = [x.strip() for x in set.split(r',')]



        # Debug
        # print(sets)
        print(cube_sets)

        for cube_set in cube_sets:
        
            # Find the number of cubes
            number_of_cubes = int(re.search(r'\d+', cube_set).group(0))

            # Find the color of the cube
            color = re.search(r'[a-z]+', cube_set).group(0)

            # Debug
            print('cube_set: ' + str(number_of_cubes) + ' ' + color)

            if color == 'red':
                red = max(number_of_cubes, red)
            elif color == 'blue':
                blue = max(number_of_cubes, blue)
            elif color == 'green':
                green = max(number_of_cubes, green)

            # print('red: ' + str(red) + '; blue: ' + str(blue) + '; green: ' + str(green))


        # Debug
        print('red: ' + str(red) + '; blue: ' + str(blue) + '; green: ' + str(green))
                
    if (red > red_limit or blue > blue_limit or green > green_limit):
        pass
    else:
        sum_of_ids += id

        

    
    # Debug
    # print(game_number)
    # print(game)
    # print(sets)

    print('----Sum of IDs: ' + str(sum_of_ids))
