i = -1
while i < 1:
    line = ''
    j = -1.6
    while j < 1.6:
        x = 0
        y = 0
        for n in xrange(20):
            x, y = 2 * x * y + i, y * y - x * x + j
        if (x * x + y * y) ** .5 < 2:
            line += "O"
        else:
            line += " "
        j += .04
    print line
    i += .1
