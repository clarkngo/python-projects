# Python 3
# In Python 3, this question doesn't apply. 
# The plain int type is unbounded.

# However, you might actually be looking for the 
# machine's word size. That's still available in 
# Python 3 as sys.maxsize.

import sys
max = sys.maxsize
min = -sys.maxsize -1

print(max) # 9223372036854775807
print(min) # -9223372036854775808
