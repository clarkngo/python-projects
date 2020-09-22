Source: https://www.codewars.com/kata/5b4e779c578c6a898e0005c5

Draw stairs

given a number n, draw stairs with 'I' n tall and n wide, with the tallest in the top left. Example (with - to represent spaces; DO NOT USE THEM IN THE SOLUTIONS! USE SPACES IN SOLUTION! the "-"s are for clarity.): draw_stairs(3) == '''I\n_I\n__I'''

For example, a 7-step stairs should be drawn like this:

const sevenStepStairs = drawStairs(7);
I
 I
  I
   I
    I
     I
      I

# my solution
def draw_stairs(n):
    string = ''
    for i in range(1, n+1):
        for j in range(1,i):
            string += ' '
        string += 'I\n'
    return string[0:-1]

# other solutions
def draw_stairs(n):
  return '\n'.join('I'.rjust(i + 1) for i in range(n))

def draw_stairs(n):
    return '\n'.join(f'{" " * i}I' for i in range(n))

draw_stairs = lambda n: '\n'.join(["{}I".format(" "*e) for e in range(n)])
