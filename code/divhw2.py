# r4 = r2//r3
# r5 = r2%r3
# r2, r3 could be + or -
# r2//0 will be r4=0, r5=0
from bcpu import *

#python code
p2 = 0
p3 = -3
p6 = 0 #sign check
p4 = 0 #resultant

if p2 < 0: #if p2 negative flip sign modify sign check
    p2 = 0 - r2
    p6 += 1

if p3 < 0: #if p3 negative flip sign modify sign check
    p3 = 0 - p3
    p6 -= 1

p5 = p2

while p5 > p3: #subtract until no p5 < p3
    p5 = p5 - p3
    p4 += 1

if p6 != 0: #if sign check is not zero flip sign on both answers
    p5 = 0 - p5
    p4 = 0 - p4


#post results
print("Result is " + str(p4) + ".")
print("Remainder is " + str(p5) + ".")

#asm code

#in class asm version
div2= """
Set(r4, 0)
Set(r5, 0)
Set(r6, 0) #sign checker if double negative should cancel to positive

# if p2 < 0 flip sign app to sign check
Addi(r11, pc, ?r2neg)
Movep(pc, r11, r2)
    Sub(r2, r4, r2)
    Addi(r6, r6, 1)
#>r2neg

# if p3 < 0 flip sign sub from sign check
Addi(r12, pc, ?r3neg)
Movep(pc, r12, r3)
    Sub(r3, r4, r3)
    Subi(r6, r6, 1)
#>r3neg

# if p3 or p2 zero
Addi(r10, pc, ?zero)
    Movez(pc, r10, r3)
    Movez(pc, r10, r2)

#>while (p2 >= p3):
# go to signcheck is p2 < p3
Addi(r13, pc, ?signcheck)
Sub(r9, r2, r3)
Moven(pc, r13, r9)
    #while part
    Sub(r2, r2, r3)
    Addi(r4,r4, 1)
    #go back up  to while
    Subi(pc, pc, ?while)

#>zero jump here if either number zero and set pre-results to zero
Set(r2, 0)
Set(r4, 0)

#>signcheck if not zero flip signs for results
Addi(r14, pc, ?endwhile)
Movez(pc, r14, r6)
Sub(r2, r5, r2)
Sub(r4, r5, r4)

#>endwhile transfer value from r2 to r5 for post
Move(r5, r2)
"""

Set(r2, 5)
Set(r3, 1)
startfast(div2)
print(geti(R[4]))
print(geti(R[5]))


