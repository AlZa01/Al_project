# Sorting the entered numbers (int) in ascending order
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if (a>b): # Comparing a and b.
    a,b = b,a # If a is greater than b, then we change the values of a and b. Now a has the value of b, and vice versa.
if (b>c): 
    # Comparing b and c (the value of b is now equal to the entered value of a, so we compare the currently biggest number (b) with c;
    # or in the case the first "if" is false - we just compare b and c as they were entered as the input data).
    b,c = c,b # If b is greater than c, then we change the values of b and c. Now b has the value of c, and vice versa.
    # If the first and second "if" were true, then c now has the biggest value. If the first "if" was false (or both of "if"), then c also has the biggest value.
    # We only now have to compare a and b (as we already know that c is the biggest number).
if (a>b): # Comparing a and b again.
    a,b = b,a # If a is greater than b, then we change the values of a and b. Now a has the value of b, and vice versa. And now a is the smallest number.
print('Sorted abc:', a, b, c) # Printing the result in accordance with the conclusion that c is the largest number and a is the smallest.