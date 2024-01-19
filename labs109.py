# Lab answers for CCPS109 by Puneet Birdi
# Winter 2024 Semester at Toronto Metropolitan University


# 1. Ryerson Letter Grade
def ryerson_letter_grade(pct):
    if pct < 50:
        return 'F'
    elif pct > 89:
        return 'A+'
    elif pct >= 85 and pct < 90:
        return 'A'
    elif pct >= 80 and pct < 85:
        return 'A-'

    letter = None
    symbol = None

    first_digit = pct // 10
    second_digit = pct % 10

    if first_digit >= 8:
        letter = 'A'
    elif first_digit >= 7 and first_digit < 8:
        letter = 'B'
    elif first_digit >= 6 and first_digit < 7:
        letter = 'C'
    elif first_digit >= 5 and first_digit < 6:
        letter = 'D'
    elif first_digit < 5:
        letter = 'F'

    if second_digit < 3:
        symbol = "-"
    elif second_digit > 6:
        symbol = "+"
    else:
        symbol = ""

    result = letter + symbol
    return(result)

# 2. Ascending List
def is_ascending(items):
    if len(items) <= 1:
        return True

    result = True
    for idx, i in enumerate(items):
        if (idx + 1) != len(items):
            if i >= items[idx + 1]:
                result = False

    return result

# 3. Riffle Shuffle Kerfuffle
def riffle(items, out=True):
    if len(items) == 0:
        return []

    total_length = len(items)
    mid_index = int(total_length / 2)

    first_half = items[:total_length//2]
    second_half = items[total_length//2:]
    result = []

    for i in range(total_length // 2):
        if out == True:
            result.append(first_half[i])
            result.append(second_half[i])
        else:
            result.append(second_half[i])
            result.append(first_half[i])

    return result

from math import log

# 4. Even The Odds
def only_odd_digits(n):
    num_of_digits = int(log(n, 10)) + 1

    remaining = n
    subject = None
    result = True

    for i in range(num_of_digits):
        subject = remaining%10
        remaining = remaining//10

        if subject%2 == 0:
            result = False
            return result

    return result


