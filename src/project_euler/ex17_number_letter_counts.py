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


from itertools import accumulate
lt_twenty = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

decs = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'
}


def make_dec(number):
    if number < 20:
        return lt_twenty[number]
    return f'{decs[number // 10]} {lt_twenty[number % 10]}'


assert make_dec(6) == 'six'
assert make_dec(13) == 'thirteen'
assert make_dec(45) == 'forty five'


def make_hun(number):
    h = lt_twenty[number // 100]
    d = make_dec(number % 100)
    if not h:
        return lt_twenty[0]
    return f'{h} hundred and {d}'.rstrip()


assert make_hun(342) == 'three hundred and forty two'
assert make_hun(516) == 'five hundred and sixteen'
assert make_hun(908) == 'nine hundred and eight'


def make_tou(number):
    t = lt_twenty[number // 1000]
    h = make_hun(number % 1000)
    return f'{t} tousand {h}'.rstrip()


assert make_tou(1000) == 'one tousand'


def number_to_word(number):
    ret = str()
    if number < 100:
        ret = make_dec(number)
    if 100 <= number < 1000:
        ret = make_hun(number)
    if number > 1000:
        ret = make_tou(number)
    return len(ret.replace(' ', ''))


assert number_to_word(342) == 23
assert number_to_word(115) == 20

p = max(accumulate(number_to_word(n) for n in range(0, 1000)))
print(p)
