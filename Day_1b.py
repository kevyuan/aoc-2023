import re

results = []

# with open('Day_1b_sample.txt') as f:
#     inputs = f.read().splitlines()

with open('Day_1a_input.txt') as f:
    inputs = f.read().splitlines()

calibration_value = 0
sum = 0
result = ''






line = 0

for input in inputs:

    x = 0
    first = ''
    last = ''
    length = len(input)
    line += 1

    print(input)

    # Scan the string forward
    while (x < length+1):
        print(input[0:x])
        # If a digit is found, take it 
        if re.search(r'\d', input[0:x]) is not None:
            # print('test at x: ' + test[x-1])
            first = input[x-1]
            x = length+1 # Break the loop
        
        # If not, do the scanned characters resemble a number spelled out in letters?
        elif re.search(r'one', input[0:x]) is not None:
            first = 1
            x = length+1 # Break the loop
        elif re.search(r'two', input[0:x]) is not None:
            first = 2
            x = length+1 # Break the loop
        elif re.search(r'three', input[0:x]) is not None:
            first = 3
            x = length+1 # Break the loop
        elif re.search(r'four', input[0:x]) is not None:
            first = 4  
            x = length+1 # Break the loop
        elif re.search(r'five', input[0:x]) is not None:
            first = 5
            x = length+1 # Break the loop
        elif re.search(r'six', input[0:x]) is not None:
            first = 6
            x = length+1 # Break the loop
        elif re.search(r'seven', input[0:x]) is not None:
            first = 7
            x = length+1 # Break the loop
        elif re.search(r'eight', input[0:x]) is not None:
            first = 8
            x = length+1 # Break the loop
        elif re.search(r'nine', input[0:x]) is not None:
            first = 9
            x = length+1 # Break the loop
        
        # Increment
        x += 1

    print('first: ' + str(first))

    x = 0
    # print('length :' + str(length))

    # Scan the string backwards
    while (x < length+1):
        print(input[length-x:length])
        # If a digit is found, take it 
        if re.search(r'\d', input[length-x:length]) is not None:
            # print('test at x: ' + test[x-1])
            last = input[length-x]
            x = length+1 # Break the loop
        
        # If not, do the scanned characters resemble a number spelled out in letters?
        elif re.search(r'one', input[length-x:length]) is not None:
            last = 1
            x = length+1 # Break the loop
        elif re.search(r'two', input[length-x:length]) is not None:
            last = 2
            x = length+1 # Break the loop
        elif re.search(r'three', input[length-x:length]) is not None:
            last = 3
            x = length+1 # Break the loop
        elif re.search(r'four', input[length-x:length]) is not None:
            last = 4  
            x = length+1 # Break the loop
        elif re.search(r'five', input[length-x:length]) is not None:
            last = 5
            x = length+1 # Break the loop
        elif re.search(r'six', input[length-x:length]) is not None:
            last = 6
            x = length+1 # Break the loop
        elif re.search(r'seven', input[length-x:length]) is not None:
            last = 7
            x = length+1 # Break the loop
        elif re.search(r'eight', input[length-x:length]) is not None:
            last = 8
            x = length+1 # Break the loop
        elif re.search(r'nine', input[length-x:length]) is not None:
            last = 9
            x = length+1 # Break the loop
        
        # Increment
        x += 1

    print('last: ' + str(last))

    # Build the result string by taking the first and the last character
    print(f'Result: {first}{last}')

    calibration_value = int(f'{first}{last}')
    sum += calibration_value
    print()

print(line)
print(sum)


output = open('Day_1b_output.txt', 'w')
output.write(str(sum))
output.close()