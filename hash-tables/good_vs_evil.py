# Description
# Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. Different races will certainly be involved. Each race has a certain worth when battling against others. On the side of good we have the following races, with their associated worth:

# Hobbits: 1
# Men: 2
# Elves: 3
# Dwarves: 3
# Eagles: 4
# Wizards: 10
# On the side of evil we have:

# Orcs: 1
# Men: 2
# Wargs: 2
# Goblins: 2
# Uruk Hai: 3
# Trolls: 5
# Wizards: 10
# Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side of good and compare it with the worth of the side of evil, the side with the larger worth will tend to win.

# Thus, given the count of each of the races on the side of good, followed by the count of each of the races on the side of evil, determine which side wins.

# Input:
# The function will be given two parameters. Each parameter will be a string separated by a single space. Each string will contain the count of each race on the side of good and evil.

# The first parameter will contain the count of each race on the side of good in the following order:

# Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
# The second parameter will contain the count of each race on the side of evil in the following order:

# Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
# All values are non-negative integers. The resulting sum of the worth for each side will not exceed the limit of a 32-bit integer.

# Output:
# Return "Battle Result: Good triumphs over Evil" if good wins, "Battle Result: Evil eradicates all trace of Good" if evil wins, or "Battle Result: No victor on this battle field" if it ends in a tie.

# Test.assert_equals(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'),  'Battle Result: Evil eradicates all trace of Good', 'Evil should win')
# Test.assert_equals(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'), 'Battle Result: Good triumphs over Evil', 'Good should win')
# Test.assert_equals(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'),  'Battle Result: No victor on this battle field', 'Should be a tie')

def goodVsEvil(good, evil):
    # Go get'em boys...
    good_dict = {
        '0': 1,   # Hobbits
        '1': 2,   # Men
        '2': 3,   # Elves
        '3': 3,   # Dwarves
        '4': 4,   # Eagles
        '5': 10   # Wizards
    }

    evil_dict = {
        '0': 1,   # Orcs
        '1': 2,   # Men
        '2': 2,   # Wargs
        '3': 2,   # Goblins
        '4': 3,   # Uruk Hai
        '5': 5,   # Trolls
        '6': 10   # Wizards
    }

    good_list = good.split(' ')
    evil_list = evil.split(' ')

    good_sum = 0
    evil_sum = 0

    for i in range(len(good_list)):
        good_sum += good_dict[str(i)] * int(good_list[i])

    for j in range(len(evil_list)):
        evil_sum += evil_dict[str(j)] * int(evil_list[j])

    if good_sum > evil_sum:
        return 'Battle Result: Good triumphs over Evil'
    elif evil_sum > good_sum:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:   # good_sum == evil_sum
        return 'Battle Result: No victor on this battle field'

# better solution
def goodVsEvil2(good, evil):

    points_good = [1, 2, 3, 3, 4, 10]
    points_evil = [1, 2, 2, 2, 3, 5, 10]

    good = sum([int(x)*y for x, y in zip(good.split(), points_good)])
    evil = sum([int(x)*y for x, y in zip(evil.split(), points_evil)])

    result = 'Battle Result: '

    if good < evil:
        return result +'Evil eradicates all trace of Good'
    elif good > evil:
        return result + 'Good triumphs over Evil'
    else:
        return result + 'No victor on this battle field'

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(
          goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'),
          'Battle Result: Evil eradicates all trace of Good',
          'Evil should win')

    def test2(self):
        self.assertEqual(
          goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'),
          'Battle Result: Good triumphs over Evil',
          'Good should win')

    def test3(self):
        self.assertEqual(
          goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'),
          'Battle Result: No victor on this battle field',
          'Should be a tie')

if __name__ == '__main__':
    unittest.main()
