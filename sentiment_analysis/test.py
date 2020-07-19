


def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn(100)
# Call the fucntion so that it returns True and assign it to the variable c_true
c_false = checkingIfIn(100)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
print(checkingIfIn('apple'))
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check


