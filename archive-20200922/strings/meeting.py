# https://www.codewars.com/kata/meeting/python

# Meeting

# John has invited some friends. His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
# Could you make a program that

# makes this string uppercase
# gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

# So the result of function meeting(s) will be:

# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
# It can happen that in two distinct families with the same family name two people have the same first name too.

# my solution
def meeting(s):
    lst = []
    for name in s.split(';'):
        lst.append(name.split(':'))
    for i in range(len(lst)):
        lst[i][0], lst[i][1] = lst[i][1].upper(), lst[i][0].upper()
    lst.sort()
    st = ''
    for j in range(len(lst)):
        st += '('+ lst[j][0] + ', ' + lst[j][1] + ')'
    return st

# other solution
def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))
