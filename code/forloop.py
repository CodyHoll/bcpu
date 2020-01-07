from bcpu import *

# FOR LOOP
# python

def pythonFor():
    counter = 0
    p3 =3

    while(counter < 10):
        # do someting
        p3 += 1

        # increment counter
        counter += 1

# FOR LOOP
# assembly
forloop = """
#:counter = r2
Set(counter, 0)
Set(r3, 3)

#>while (p2 < 0):
# go to endwhile if not true (counter >= 10)
Subi(r9, counter, 10)
Addi(r10, pc, ?endwhile) #r10 = addr of endwhile
Movep(pc, r10, r9) #goto endwhile if r2 != 0
    # while part
    Addi(r3, r3, 1)
    Addi(counter, counter, 1)
    # go back to while
    Subi(pc, pc, ?while)
#>endwhile
"""
# expect r2 = 10, r3 = 13

start(forloop)
printr()
printm()
