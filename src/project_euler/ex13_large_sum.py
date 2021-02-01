"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

ex13_data.txt
"""

# def get_number():

sum_ = int()

with open("ex13_data.txt") as f:
    for ff in f.readlines():
        sum_ += int(ff)
        
print(str(sum_)[:10])
