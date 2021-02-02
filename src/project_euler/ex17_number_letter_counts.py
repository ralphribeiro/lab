"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

"""
from collections import deque


lt_twenty = {
    0: '', 1: 'one', 2: 'two', 3: 'trhee', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fiveteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

decs = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'
}

def number_to_word(number):
    ret = deque()
    if 1 <= number < 20:
        print(lt_twenty[number])
    if 20 <= number < 100:
        r = f'{decs[number // 10]} {lt_twenty[number % 10]}'
        print(r)
    if 100 <= number < 1000:
        r = f'{lt_twenty[number // 100]} handred {decs[number // 100]} {lt_twenty[number % 100]}'
        print(r)


# for i in range(95):
number_to_word(245)
    




