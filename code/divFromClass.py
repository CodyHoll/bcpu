from bcpu import *
########################################### CODE FROM CLASS ###########################################
c2 = 9
c3 = 2
c6 = 0 #sign check
c4 = 0
#c5 = 0 # wasn't specfied

if c2 < 0: # if c2 neg, flip sing and modify sign chekc
    c2 = 0 - c2
    c6 += 1

if c3 <0: # if c3 neg, flip sign, modify sign check
    c3 = 0 - c3
    c6 -= 1

c5 = c2

while c5 >= c3: # sub until no c5 < c3
    c5 = c5 - c3
    c4 += 1

if c6 != 0: # if sign check is not zero flip sign on both answers
    c5 = 0 - c5
    c4 = 0 - c4

# post results
print("c4: {}".format(c4))
print("c5: {}".format(c5))

# asm CODE
asm = """
Set(r4,0)
Set(r5,0)
Set(r6, 0) # sign checker if doubleneg should cancel to pos

# if r2 < 0 flip sign app to sign check
Addi(r11, pc, ?r2neg)
Movep(pc, r11,r2)
    Sub(r2,r4,r2)
    Addi(r6,r6,1)
#>r2neg

# if r3 < 0 flip sign sub from sign check
Addi(r12, pc, ?r3neg)
Movep(pc, r12,r3)
    Sub(r3,r4,r3)
    Subi(r6,r6,1)
#>r3neg

# if r3 or r2 zero
Set(r10, ?zero)         # idk
Add(r10, pc, r10)       # idk
Subi(r10,r10,1)         # idk <- Q: why subtract that shit A: can 'goto' a differnet spot than specified. One valid line of code above '?zero' in this case.
Movez(pc, r10, r3)
Movez(pc, r10, r2)

#>while (r2 >= r3):
# goto sighcheck is r2 < r3
Addi(r13,pc,?signcheck)
Sub(r9,r2,r3)
Moven(pc,r13,r9)
    # while body
    Sub(r2,r2,r3)
    Addi(r4,r4,1)
    # go back up to while
    Subi(pc,pc,?while)     # removed this
    #Set(r12,?while+1)       # added this
    #Sub(pc,pc,r12)          # added this

#>zero jump here if either number zero and set pre-results to zero
Set(r2,0)
Setr4,0)

#>signcheck if not zero flip signs for results
Addi(r14,pc,?endwhile)
Movez(pc,r14,r6)
Sub(r2,r5,r2)
Sub(r4,r5,r4)

#>endwhile transfer value from r2 to r5 for post
Move(r5,r2)

"""

Set(r2,8)
Set(r3,2)

load(asm, fname='divFromClass')
runfast()

# simulate print
print(geti(R[4]))
print(geti(R[5]))
