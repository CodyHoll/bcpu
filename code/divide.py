# div p4 = p2//p3 (integer divider)
# p5 = p2%p3 (remainder)

# don't forget divided by 0 is undefined (set to -1)

# div p4 = p2/p3
from bcpu import *

# use python to find intended results
# -5//2 = -3
# -5//-2 = 2
# -5%-2 = -1
#-4/3 = -1 ,with remainder of -1


# input
p2 = -5
p3 = -2

p4 = 7
p5 = 4


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


# ASSEMBLY

##div = """
##Set(r2, 6)
##Set(r3, 5)
##Set(r4, 0)
##Set(r5, 0)
##
###>while r2!=0:
### goto endwhile if r2 <= 0
##Subi(r10, pc, ?endwhile) # saving address of endwhile in r10
##Movez(pc, r10, r2)
##    # while part
##    Addi(r4, r4, 1)
##    Sub(r2, r2, r3)
##    # go back up to while
##    Subi(pc, pc, ?while)
###>endwhile
##Moven(r4, r4) # print
##
##"""

div2 = """
Set(r2, 8)
Set(r3, 2)

Set(r4, 0)
Subi(r4, r4, 1) # set r4 to -1
Set(r5, 0)
Subi(r5, r5, 1) # set r5 to -1

#if1 (p3 != 0):
# go end if p3 == 0
Addi(r11, pc, ?end)
Movez(pc, r11, r3)

    Set(r4, 0)
    Set(r5, 0)

    #if2 (p2 > 0):
    # goto end else when (p2 <= 0)
    Addi(r11, pc, ?else)

        #>while1 (r2 > r3):
        # goto endwhile1 if r2 <= r3
        Sub(r9, r2, r3)
        Addi(r10, pc, ?endwhile1)
        Moven(pc, r10, r9)
            # while part
            Sub(r2, r2, r3)

            #if3 (r2 >= 0):
            # goto endif3 if (p2 < 0)
            Addi(r11, pc, ?endif3)
            Moven(pc, r11, r2)
                Addi(r4, r4, 1)
            #>endif3

            Addi(r5, r2, r3)

            # go back up to while1
            Subi(pc, pc, ?while1)
        #>endwhile1

    #>else :
        #>while2 (r2 < 0)
        # goto endwhile2 when (r2 >= 0):
        Addi(r10, pc, ?endwhile2)
        Movep(pc, r10, r2)

        Add(p2, p2, p3)
        # if4 (r2 <= 0)
        # goto endif4 when (r2 > 0)
        Set(r0, 0)
        Sub(r9, r0, r2)
        Addi(r10, pc, ?endif4)
        Moven(pc, r10, r9)
            Subi(r4, r4, 1)
        #>endif4
            Sub(r5, r2, r3)
        #>endwhile2

    Move(r5, r2)
#>end



Move(r4, r4)
Move(r5, r5)
"""

#start(div2)
