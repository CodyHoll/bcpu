# mul p4 = p2*p3
from bcpu import *

# input
p2 = -10
p3 = -5

# output p4
p4 = 0


while (p2 > 0):
    p2 -= 1
    p4 = p3 + p4
    # go back up to while
# endwhile
while (p2 < 0):
    p2 += 1
    p4 = p4 - p3
    # go back up to while
# endwhile

print (p4)


# had counter of n originally,
# but can decrement p2 instead to save registers

# ASSEMBLY

##mul = """
##Set(r2, 0)
##Set(r3, 0)
##Set(r4, 0)
##
###>while r2!=0:
### goto endwhile if p2 == 0
##Addi(r10, pc, ?endwhile) # saving address of endwhile in r10
##Movez(pc, r10, r2)
##    # while part
##    Add(r4, r4, r3)
##    Subi(r2, r2, 1)
##    # go back up to while
##    Subi(pc, pc, ?while)
###>endwhile
##Move(r4, r4) # print
##
##"""
##
###start(mul)

# HOMEWORK MAKE MULITPLY AND DIVISION PROGRAMS WORK WITH NEGATIVES

mul = """
Set(r2, 4)
Set(r3, 0)

Set(r4, 0)

#>while r2>0:
# goto endwhile if p2 == 0
Addi(r10, pc, ?endwhile) # saving address of endwhile in r10
Movez(pc, r10, r2)
    # while part
    Add(r4, r4, r3)
    Subi(r2, r2, 1)
    # go back up to while
    Subi(pc, pc, ?while)

#>while r2<0:
# goto endwhile if p2 == 0
Addi(r10, pc, ?endwhile) # saving address of endwhile in r10
Moven(pc, r10, r2)
    # while part
    Sub(r4, r4, r3)
    Addi(r2, r2, 1)
    # go back up to while
    Subi(pc, pc, ?while)
#>endwhile
Move(r4, r4) # print

"""

start(mul)
