# Counting the number of str elements in the list
res = 0 # Initializing counter by setting res to 0.
count = [23, 'Hello', 34.56, True, ['apple', 'mango', 'banana']] # Creating the list with elements of different types (now there is 1 string in this list).
for i in count: # Using the "for" loop to iterate through each element in count. 
    if type(i) == str: # With condition checking if the current element is a string.
        res += 1 # If it is, then the counter (res) is incremented.
print('The number of string elements in the list:', res) # Printing the result (final count of string elements).