# https://www.codewars.com/kata/565f5825379664a26b00007c/train/python

# Surface Area and Volume of a Box

# Write a function that returns the total surface area and volume of a box as an array: [area, volume]

def get_size(w,h,d):
    return [2 * (h * w) + 2 * (h * d) + 2 * (w * d), w*h*d]
