import re

results = []

with open('Day_1b_sample.txt') as f:
    inputs = f.read().splitlines()

calibration_value = 0
sum = 0
result = ''


test = inputs[0]

x = 0
first = ''
last = ''
length = len(test)

# Scan the string forward
while (x < length):
    print(test[0:x])
    # If a digit is found, take it 
    if re.search(r'\d', test[0:x]) is not None:
        # print('test at x: ' + test[x-1])
        first = test[x-1]
        x = length # Break the loop
    
    # If not, do the scanned characters resemble a number spelled out in letters?
    elif re.search(r'one', test[0:x]) is not None:
        first = 1
        x = length # Break the loop
    elif re.search(r'two', test[0:x]) is not None:
        first = 2
        x = length # Break the loop
    elif re.search(r'three', test[0:x]) is not None:
        first = 3
        x = length # Break the loop
    elif re.search(r'four', test[0:x]) is not None:
        first = 4  
        x = length # Break the loop
    elif re.search(r'five', test[0:x]) is not None:
        first = 5
        x = length # Break the loop
    elif re.search(r'six', test[0:x]) is not None:
        first = 6
        x = length # Break the loop
    elif re.search(r'seven', test[0:x]) is not None:
        first = 7
        x = length # Break the loop
    elif re.search(r'eight', test[0:x]) is not None:
        first = 8
        x = length # Break the loop
    elif re.search(r'nine', test[0:x]) is not None:
        first = 9
        x = length # Break the loop
      
    # Increment
    x += 1

print('first: ' + str(first))

x = 0
print('length :' + str(length))

# Scan the string backwards
while (x < length):
    print(test[length-x:length])
    # If a digit is found, take it 
    if re.search(r'\d', test[length-x:length]) is not None:
        # print('test at x: ' + test[x-1])
        last = test[x]
        x = length # Break the loop
    
    # If not, do the scanned characters resemble a number spelled out in letters?
    elif re.search(r'one', test[length-x:length]) is not None:
        last = 1
        x = length # Break the loop
    elif re.search(r'two', test[length-x:length]) is not None:
        last = 2
        x = length # Break the loop
    elif re.search(r'three', test[length-x:length]) is not None:
        last = 3
        x = length # Break the loop
    elif re.search(r'four', test[length-x:length]) is not None:
        last = 4  
        x = length # Break the loop
    elif re.search(r'five', test[length-x:length]) is not None:
        last = 5
        x = length # Break the loop
    elif re.search(r'six', test[length-x:length]) is not None:
        last = 6
        x = length # Break the loop
    elif re.search(r'seven', test[length-x:length]) is not None:
        last = 7
        x = length # Break the loop
    elif re.search(r'eight', test[length-x:length]) is not None:
        last = 8
        x = length # Break the loop
    elif re.search(r'nine', test[length-x:length]) is not None:
        last = 9
        x = length # Break the loop
      
    # Increment
    x += 1

print('last: ' + str(last))




# for input in inputs:

#     x = 0
#     length = len(input)

#     # Scan the string forward
#     while (x < length):
#         print(input[0:x])
#         x += 1

        # If a digit is found, take it 

        # If not, do the scanned characters resemble a number spelled out in letters?

    # Get rid of all the letters
    # input = re.sub(r'[one]', '1', input)
    # input = re.sub(r'[two]', '2', input)
    # input = re.sub(r'[three]', '3', input)
    # input = re.sub(r'[four]', '4', input)
    # input = re.sub(r'[five]', '5', input)
    # input = re.sub(r'[six]', '6', input)
    # input = re.sub(r'[seven]', '7', input)
    # input = re.sub(r'[eight]', '8', input)
    # input = re.sub(r'[nine]', '9', input)
    # input = re.sub(r'[a-zA-Z]', '', input)

    # print('input :' + input)




    

    # Build the result string by taking the first and the last character
    # result = f'Result: {temp[0]}{temp[-1]}'
    # print(result)

    # calibration_value = int(f'{input[0]}{input[-1]}')
    # sum += calibration_value

# print(sum)

output = open('Day_1b_output.txt', 'w')
output.write(str(sum))
output.close()