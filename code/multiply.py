from bcpu import *
# Cody Holland

# python code

# input
p2 = -2
p3 = 3

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

print(p4)

def mulp(p2:int, p3:int)->'p4:int':
    a=1

# assembly language code
mul = """
#Set(r2, 2)
#Subi(r2, r2, 4)
#Set(r3, 3)

#>mul(r2,r3)->p4

# takes input r2, r3
# gives output r4

Set(r4, 0)

#>while1 p2 > 0:
# goto endwhile if p2 <= 0

Set(r0,0)
Set(r5,0)
Sub(r5, r0, r2)
Addi(r10, pc, ?endwhile1) # save addr of endwhile to r10
Movep(pc, r10, r5)        # goto endwhile if r2 <= 0
    #while part
    Add(r4, r4, r3)
    Subi(r2, r2, 1)
    # goto while
    Subi(pc, pc, ?while1)

#>endwhile1

# -------- Second While ----------

#>while2 p2 < 0:
# goto endwhile if p2 >= 0

Addi(r10, pc, ?endwhile2) # save addr of endwhile to r10
Movep(pc, r10, r2)        # goto endwhile if r2 >= 0
    #while part
    Sub(r4, r4, r3)
    Addi(r2, r2, 1)
    # goto while
    Subi(pc, pc, ?while2)

#>endwhile2
Move(r4,r4) # simulate print

"""
#--------------- Syntax for running the file/function -----------------

# Set(r2,2)
# Set(r3,3)
# start(mul)

# OR

Set(r2, 2)
Set(r3, 3)
load(mul, fname='mul')
runfast()
# simulate print
print(geti(R[4]))


#div p4 = p2//p3    #integer division
#p5 = p2%p3         #remainder

# Consider 5/2 deeply

# MIDTERM QUESTIONS
#1) r5 = 5000 + r2*r3 - r4
    # r2,r3, r4 are inputs
    # r5 is the outputr

#2)
