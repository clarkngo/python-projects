color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
myfile = open('Color.txt', "w")
for c in color:
    myfile.write("{}\n".format(c))
myfile.close()
