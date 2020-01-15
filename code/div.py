# r4 = r2//r3
# r5 = r2%r3
# r2, r3 could be + or -

# use python to find intended results
# -5//2 = -3
# -5//-2 = 2
# -5%-2 = -1
#-4/3 = -1 ,with remainder of -1

# if divided by zero make it equal
# r4 = 0 AND r5 = 0 -------------- => r2//0 yields.. .r4 =0, r5 = 0

# python code
# input
p2 = 9
p3 = 2

p4 = 0
p5 = 0

if p3 != 0:
    # I think I can combine shit and make it look like 'mul' from in class. 

    # if numerator is positive
        # do pos stuff
    # else (numerator is neg)
        # do neg stuff


if p3 != 0:
    p4 = 0
    p5 = 0
    if p2 > 0:
        while (p2 > 0):
            p2 = p2 - p3
            if (p2 >= 0):
                p4 += 1
            else:
                p5 = p2 + p3
            # go back up to while
        # endwhile
    else:
        while(p2 < 0):
            p2 = p2 + p3
            if (p2 <= 0):
                p4 -= 1
            else:
                p5 = p2 - p3

print (p4) # value
print (p5) # remainder
