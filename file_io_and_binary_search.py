import math

# read in a text file of airplane crash data
aviation_data = []

with open('AviationData.txt', 'r') as my_file:
    for line in my_file:
        aviation_data.append(line)
        
aviation_list = []

# split data on the pipe character
for row in aviation_data:
    new_row = row.split('|')
    aviation_list.append(new_row)

aviation_columns = aviation_list[0][:]
aviation_list = aviation_list[1:][:]

lax_code = []

# search for a specific flight accident
for r in aviation_list:
    for field in r:
        if field.strip() == 'LAX94LA336':
            lax_code.append(r)
                
# the quadratic search algorithm written above does not take too long to return a row
# however, other search algorithms may be faster, if the data set is sorted 
# or formatted correctly

# tokenize every non Null string in the data set
all_tokens = []

for i in aviation_list:
    for w in i:
        if w is not None:
            all_tokens.append(w.strip())

# sort tokens in alphabetical order
sorted_tokens = sorted(all_tokens, key=str.lower)
            
# implement a binary search algorithm in log time complexity
def binary_search(string):
    length = len(sorted_tokens)
    upper_bound = length - 1
    lower_bound = 0
    index = math.floor(length / 2)
    guess = sorted_tokens[index].strip()
    
    while string != guess and upper_bound >= lower_bound:
        if string < guess:
            upper_bound = index - 1
            index = math.floor(upper_bound / 2)
            guess = sorted_tokens[index].strip()
        else:
            lower_bound = index + 1
            index = math.floor((upper_bound + lower_bound) / 2)
            guess = sorted_tokens[index].strip()
            
    if string == guess:
        return guess
    else:
        return -1
    
print(binary_search('LAX94LA336'))

# the binary search algorithm is much faster accessing the searched value
# however, the preprocessing of the data takes a fair amount of time

# create list of dictionaries to store the data
aviation_dict_list = []

for row in aviation_data:
    new_row = row.split('|')
    new_dict = {}
    
    for i in range(len(new_row)):
        new_dict[aviation_columns[i]] = new_row[i]

    aviation_dict_list.append(new_dict)

# find a specific accident by iterating through dictionary values
lax_dict = []

for d in aviation_dict_list:
    for k, v in d.items():
        if v.strip() == 'LAX94LA336':
            lax_dict.append(d)

print(lax_dict)

create and write to a new text file
file = open('dictionary_thoughts.txt', 'w')
file.write('In my opinion, using a dictionary to search for a value (as opposed to a list of lists) is about the same effort, because you still have to write a nested for loop to iterate through the list of dictionaries')