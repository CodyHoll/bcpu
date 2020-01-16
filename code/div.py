from bcpu import *
# NOTE: if denomorator or numerator is 0, outputs should be 0.

# python code
# inputs
p2 = 9
p3 = 2

# outputs
p4 = 0
p5 = 0

print("Running python code: {}/{}".format(p2,p3))
try:
    print("Python expected output: p4 = {}, p5 = {}".format(p2//p3,p2%p3))
except:
    print("cant div that")

# if denominator is 0, throw error
if p3 != 0:
    # if both are pos (not neg)
    if(p2 >= 0 and p3 > 0):
        # if denum is greater
        p5 = p2
        # if num is greater
        while(p2 >= p3): 
            p4 = p4 + 1
            p2 = p2 - p3
            p5 = p2

    # if both are neg
    elif(p2 <= 0 and p3 < 0):
        # if denum is greater
        p5 = p2
        #if num is greater
        while(p2 <= p3):
            p4 = p4 + 1
            p2 = p2 - p3
            p5 = p2

    # if ONLY num is pos
    elif(p2 >=0 and p3 < 0):
        #if either is greater
        while(p2 > 0):
            p4 = p4 - 1
            p2 = p2 + p3
            p5 = p2

    # if ONLY denum is pos
    else:
        # if either is greater
        while(p2 < 0):
            p4 = p4 - 1
            p2 = p2 + p3
            p5 = p2

print("Python actual output:   p4 = {}, p5 = {}".format(p4,p5))
print()
print("Running asm code: ")

div = """
# takes inputs r2, r3
# gives outputs r4, r5
#>div(r2,r3)->r4,r5

Set(r4, 0)
Set(r5, 0)

Set(r0,0)
Set(r12, ?end) # r12 will hold the value for jumps to the end

Add(r10, pc, r12)
Movez(pc, r10, r2)
Movez(pc, r10, r3)

    Set(r13, ?endif1)
    Add(r10, pc, r13)
    Moven(pc, r10, r2)      # goto endif1 if (r2 < 0)
        # r2 is pos.... check r3
        Addi(r10, pc, ?endif2)
        Moven(pc, r10, r3)  # goto endif2 if (r3 < 0)
            # -------- CODE r2 pos, r3 pos -----
            Move(r5, r2)

            #>while1 (r2 >= r3)
            Sub(r11, r2, r3)
            Addi(r10,pc,?endwhile1)
            Moven(pc, r10, r11)      # if (r2>= r3) is False... (r2<r3)
                # while body
                Addi(r4,r4,1)
                Sub(r2,r2,r3)
                Move(r5,r2)

                Subi(pc, pc, ?while1)

            #>endwhile1

            # jump to end (which is r12)
            Add(pc,pc,r12)

        #>endif2
        # -------- CODE r2 pos, r3 neg -----
        #>while2 (r2>=0)
        Addi(r10, pc, ?endwhile2)
        Moven(pc, r10, r2)      # if (r2>=0) is False... (r2<0)
            # while body
            Subi(r4,r4,1)
            Add(r2,r2,r3)
            Move(r5,r2)

            Subi(pc,pc,?while2)

        #>endwhile2

        # jump to end (which is r12)
        Add(pc,pc,r12)

    #>endif1 (r2 is negative or 0)
    #it's now safe to say that (r2 <= 0)

    # It seems to me the case that r10 has to be reset before being used by pc again??
    Set(r10, 0) ### <-- IDK WHY THIS LINE OF CODE IS NESSECARY ###

    Addi(r10, pc, ?endif3)
    Moven(pc, r10, r3)      # if r3 is neg (r3 < 0)
        #-------- CODE r2 neg, r3 pos -----
        #>while3 (r2 < 0)
        Addi(r10, pc, ?endwhile3)
        Movep(pc, r10, r2)      # if (r2<0) is False..... (r2>=0)
            # while body
            Subi(r4,r4,1)
            Add(r2,r2,r3)
            Move(r5,r2)

            Subi(pc,pc,?while3)

        #>endwhile3

        # jump to end (which is r12)
        Add(pc,pc,r12)

    #>endif3 
    # -------- CODE r2 neg, r3 neg -----
    Move(r5, r2)

    #>while4 (r2 <= r3)
    Sub(r11,r3,r2)
    Addi(r10,pc,?endwhile4)
    Moven(pc,r10, r11)     # if (r2<=r3) is False..... (r2>r3)
        # while body
        Addi(r4,r4,1)
        Sub(r2,r2,r3)
        Move(r5,r2)

        Subi(pc,pc,?while4)

    #>endwhile4

#>end
"""


# HERE IS WHERE YOU CHANGE INPUT (r2 AND r3)
Set(r2, 9)
#Sub(r2,r0,r2)
Set(r3, 2)
#Sub(r3,r0,r3)
load(div, fname='div')
runfast()

# simulate print
print(geti(R[4]))
print(geti(R[5]))