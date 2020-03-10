# datetime.date()
# Return date object with same year, month and day.


###datetime.strptime(input_text, "%d %m %Y")
#!/usr/bin/env python3

from datetime import datetime, date

print("Your date of birth (dd-mm-yyyy)")
date_of_birth = datetime.strptime(input("--->"), "%d-%m-%Y")

def calculate_age(born):
    today = date.today()
    nogNietJarigInHuidigJaar = (today.month, today.day) < (born.month, born.day)

    if nogNietJarigInHuidigJaar:
        leeftijd = today.year - born.year - 1
    else:
        leeftijd = today.year - born.year

    return leeftijd

# age = calculate_age(date_of_birth)


# print(age)

# https://stackoverflow.com/questions/5292303/how-does-tuple-comparison-work-in-python

# Tuples are compared position by position: the first item of the first tuple is 
# compared to the first item of the second tuple; if they are not equal (i.e. the first is
# greater or smaller than the second) then that's the result of the comparison, else the 
# second item is considered, then the third and so on.

# Note 1: < and > do not mean "smaller than" and "greater than" but "is before" and "is after": 
# so (0, 1) "is before" (1, 0).

# Note 2: tuples must not be considered as vectors in a n-dimensional space, compared according to their length.

# Note 3: referring to question https://stackoverflow.com/questions/36911617/python-2-tuple-comparison: 
# do not think that a tuple is "greater" than another only if any element of the first is greater than 
# the corresponding one in the second.
