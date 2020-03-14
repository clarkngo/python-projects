# Python Notes

I transitioned from Java to solve problems and learn from them quicker.

## Variables
- no concept of declaration
- variable data type is decided at run time depending of the value it is being referred to
- there is really no variable

## Array

Index:

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

## List

A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are also very useful for implementing stacks and queues. Lists are mutable, and hence, they can be altered even after their creation.

### print()

```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
objects - object to the printed. * indicates that there may be more than one object
sep - objects are separated by sep. Default value: ' '
end - end is printed at last
file - must be an object with write(string) method. If omitted it, sys.stdout will be used which prints objects on the screen.
flush - If True, the stream is forcibly flushed. Default value: False
```

### range()
```
range([start], stop[, step])

start: Starting number of the sequence.
stop: Generate numbers up to, but not including this number.
step: Difference between each number in the sequence.
```

### slicing

```
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
a[start:stop:step] # start through not past stop, by step
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```
Source: https://stackoverflow.com/questions/509211/understanding-slice-notation

## Dictionary
Iterate over keys and values
```
days  = {'mon':'Monday', 'tue':'Tuesday', 'wed':'Wednesday', 'thu':'Thursday', 'fri':'Friday',
        'sat':'Saturday', 'sun':'Sunday'}

for day in days:
    print(day, days[day])
```
Output:
```
mon Monday
tue Tuesday
wed Wednesday
thu Thursday
fri Friday
sat Saturday
sun Sunday
```
## modules

### timeit
