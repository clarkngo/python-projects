https://www.codewars.com/kata/57e8f757085f7c7d6300009a/train/python

Holiday II - Plane Seating

Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.

To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters 'I' and 'J' from their seat naming system.

the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter, A-K with the exclusions mentioned above.

Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

Given a seat number, your task is to return the seat location in the following format:

'2B' would return 'Front-Left'.

If the number is over 60, or the letter is not valid, return 'No Seat!!'.

test.describe("Basic tests")
test.assert_equals(plane_seat('2B'), 'Front-Left')
test.assert_equals(plane_seat('20B'), 'Front-Left')
test.assert_equals(plane_seat('58I'), 'No Seat!!')

def plane_seat(a):
    my_dict = {
        "A" : "Left",
        "B" : "Left",
        "C" : "Left",
        "D" : "Middle",
        "E" : "Middle",
        "F" : "Middle",
        "G" : "Right",
        "H" : "Right",
        "K" : "Right",
    }
    seat = ''
    print()
    if a[-1] in my_dict:
        seat += my_dict[a[-1]]
    else:
        return 'No Seat!!'
    num = int(a[:len(a)-1])
    if num >= 1 and num <= 20:
        seat = 'Front-' + seat
    elif num >= 21 and num <= 40:
        seat = 'Middle-' + seat
    elif num >= 41 and num <= 60:
        seat = 'Back-' + seat
    else:
        return 'No Seat!!'
    return seat

def plane_seat(a):
    front, middle, back = (range(1,21), range(21,41), range(41,61))
    left, center, right = ('ABC', 'DEF', "GHK")
    x, y = ('', '')

    if int(a[:-1]) in front:    x = 'Front-'
    if int(a[:-1]) in middle:   x = 'Middle-'
    if int(a[:-1]) in back:     x = 'Back-'

    if a[-1] in left:    y = 'Left'
    if a[-1] in center:  y = 'Middle'
    if a[-1] in right:   y = 'Right'

    return x+y if all((x,y)) else 'No Seat!!'
