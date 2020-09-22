# https://www.codewars.com/kata/57d001b405c186ccb6000304/train/python

# Ironman Triathlon

# An Ironman Triathlon is one of a series of long-distance triathlon races organized by the World Triathlon Corporaion (WTC). It consists of a 2.4-mile swim, a 112-mile bicycle ride and a marathon (26.2-mile) (run, raced in that order and without a break. It hurts... trust me.

# Your task is to take a distance that an athlete is through the race, and return one of the following:

# If the distance is zero, return 'Starting Line... Good Luck!'.

# If the athlete will be swimming, return an object with 'Swim' as the key, and the remaining race distance as the value.

# If the athlete will be riding their bike, return an object with 'Bike' as the key, and the remaining race distance as the value.

# If the athlete will be running, and has more than 10 miles to go, return an object with 'Run' as the key, and the remaining race distance as the value.

# If the athlete has 10 miles or less to go, return return an object with 'Run' as the key, and 'Nearly there!' as the value.

# Finally, if the athlete has completed te distance, return "You're done! Stop running!".

# All distance should be calculated to two decimal places.

# Test.describe("Basic tests")
# Test.assert_equals(i_tri(36),{'Bike':'104.60 to go!'})
# Test.assert_equals(i_tri(103),{'Bike':'37.60 to go!'})
# Test.assert_equals(i_tri(0),'Starting Line... Good Luck!')
# Test.assert_equals(i_tri(2),{'Swim':'138.60 to go!'})
# Test.assert_equals(i_tri(151),"You're done! Stop running!")

def i_tri(s):
    TOTAL = 140.60
    rem = (TOTAL * 10 - s * 10) / 10
    rem = format(rem, '.2f')
    rem = str(rem)
    if s == 0: return 'Starting Line... Good Luck!'
    elif s > 0 and s <= 2.4: return {'Swim': rem +' to go!'}
    elif s > 2.4 and s <= 112: return {'Bike': rem +' to go!'}
    elif s > 112 and s < TOTAL - 10: return {'Run': rem +' to go!'}
    elif s > TOTAL - 10 and s < TOTAL: return {'Run': 'Nearly there!'}
    else: return "You're done! Stop running!"

def i_tri(s):
    total = 2.4 + 112 + 26.2
    to_go = '%.2f to go!' % (total - s)

    return ( 'Starting Line... Good Luck!' if s == 0 else
            {'Swim': to_go} if s < 2.4 else
            {'Bike': to_go} if s < 2.4 + 112 else
            {'Run':  to_go} if s < total - 10 else
            {'Run': 'Nearly there!'} if s < total else
            "You're done! Stop running!" )
