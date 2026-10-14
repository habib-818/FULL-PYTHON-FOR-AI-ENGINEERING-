import pandas as pd


## LAMBDA
'''
 * Lambda functions are small, anonymous, one-line functions designed for throwaway operations.

 * Using if, else in lambda:- "[Value if true] if [Condition] else [Value if False]"

 * Instead of def, a name, and a return statement, you use the lambda keyword:
 Example:
'''

# Standard function
def double_value(x):
    return x * 2

double_value(10)

# Lambda equivalent
lambda x: x * 2

# More accurete with ans
result = (lambda x: x * 2)(10)
print(result)

'''
 * 10 is the value of x
 * We need assign lamda to any variable to get the ans
'''


## Lambda with Pandas
'''
 * Here we're applying 10% discount on each value.
'''

# Creating a simple DataFrame (simulating your Pandas work)
df = pd.DataFrame({'price': [100, 200, 50]})

# Using a lambda function to multiply every row's price by 0.9
df['discounted_price'] = df['price'].apply(lambda x: x * 0.9)