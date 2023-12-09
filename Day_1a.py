import re

# results = []

with open('Day_1a_input.txt') as f:
    inputs = f.read().splitlines()

temp = ''
calibration_value = 0
sum = 0
# result = ''

for input in inputs:

    # Get rid of all the letters
    temp = re.sub(r'[a-zA-Z]', '', input)

 #   print('temp ' + temp)
    # print('what the')
    # print(input)

    # Build the result string by taking the first and the last character
    # result = f'Result: {temp[0]}{temp[-1]}'
    # print(result)

    calibration_value = int(f'{temp[0]}{temp[-1]}')
    sum += calibration_value

print(sum)

output = open('Day_1a_output.txt', 'w')
output.write(str(sum))
output.close()