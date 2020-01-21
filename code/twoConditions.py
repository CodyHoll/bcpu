from bcpu import *
# Check two conditions

# input
p2 = 2
p3 = 3

# output
p4 = 0

if p2 > 0 and p3 > 0:
    p4 = p2 + p3
else:
    p4 = p2 - p3


# HOMEWORK
# if p2 > p3 or p3 > 0:
#     p4 = p2 + p3
# else:
#     p4 = p2 - p3



###########################################

print("p4: {}".format(p4))

asm = """

# if p2 > 0 and p3 > 0:

#goto endif when p2 <= 0
Addi(r10,pc,?else)
Sub(r11,r0,r2)
Movep(pc,r10,r11)

#goto endif when p3 <= 0
Addi(r10,pc,?else)
Sub(r12,r0,r3)
Movep(pc,r10,r12)

    # IF BODY
    # if this line is reached then both conditions have been met
    Add(r4,r2,r3)

    # goto endelse unconditionally
    Addi(pc,pc,?endelse)

#>else
    # ELSE BODY
    Sub(r4,r2,r3)

#>endelse
"""

Set(r2, 2)
# Sub(r2,r0,r2)
Set(r3, 3)
# Sub(r3,r0,r3)

Set(r4, 0)

load(asm, fname='twoConditions')
runfast()

print("r2: {}".format(geti(R[2])))
print("r3: {}".format(geti(R[3])))
print("r4: {}".format(geti(R[4])))


# can set registers and run program using these commands
# R[2] = getb(-3)
# runfast()
