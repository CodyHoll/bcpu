# while loop

from bcpu import *

p2 = -3
p3 = 3
while p2 >= 0:
    p3 = p3 + 1
    p2 = p2 + 1

print(p2, p3)

# ---------------- ASM CODE -----------------

whileloop = """
Set(r2, 0)
Set(r3, 3)
Sub(r2, r2, r3) # r2 = -3

#>while p2 >= 0:

# go to endwhile if not true (p2 >= 0)
Set(r0, 0)
Sub(r9, r2, r0)
Addi(r10, pc, ?endwhile)        # address of endwhile
Movep(pc, r10, r9)              # go to endwhile if r2 != 0

    # while block
    Addi(r3, r3, 1)
    Addi(r2, r2, 1)

    # go back to while
    Subi(pc, pc, ?while)

#>endwhile
"""

start(whileloop)
printr()

# HW:
# while p2 < 0:
