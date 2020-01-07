from bcpu import *

# mul p4 = p2*p3

# input
p2 = 2
p3 = 3

# output p4

p4 = 0
while(p2 != 0):

    if(p2 > 0):
        p4 += p3
        p2 -= 1
    else:
        p4 -= p3
        p2 += 1

#print(p4)

# assembly language code
mul = """
Set(r2, 2)
Set(r3, 3)
Set(r4, 0)

#>while p2 != 0:
# goto endwhile if p2 == 0

Addi(r10, pc, ?endwhile) # save addr of endwhile to r10
Movez(pc, r10, r2)
    #while part
    Add(r4, r4, r3)
    Subi(r2, r2, 1)
    # goto while
    Subi(pc, pc, ?while)

#>endwhile

Move(r4,r4) # simulate print

"""

start(mul)

#div p4 = p2//p3    #integer division
#p5 = p2%p3         #remainder

# Consider 5/2 deeply
