from bcpu import *

# HOMEWORK
# input
p2 = 2
p3 = 3

# output
p4 = 0

if p2 > p3 or p3 > 0:
    p4 = p2 + p3
else:
    p4 = p2 - p3

print("p4: {}".format(p4))

asm = """
# if p2 > p3 or p3 > 0:

# goto ifbody when p2>p3
Sub(r11, r2, r3)
Sub(r11,r0,r11)
Addi(r10, pc, ?ifbody)
Moven(pc, r10, r11)

#OR goto ifbody when p3>0
Sub(r12,r0,r3)
Addi(r10,pc,?ifbody)
Moven(pc,r10,r12)

# goto else if you reach here (both conditions were false)
Addi(pc,pc,?elsebody)

#>ifbody
    Add(r4,r2,r3)

    # goto end
    Addi(pc,pc,?end)

#>elsebody
    Sub(r4,r2,r3)
#>end
"""
# if p2 > p3 or p3 > 0:
Set(r2,2)
Sub(r2,r0,r2)
Set(r3,3)
Sub(r3,r0,r3)

load(asm, fname='conditionHW')
runfast()

print("r2: {}".format(geti(R[2])))
print("r3: {}".format(geti(R[3])))
print("r4: {}".format(geti(R[4])))
