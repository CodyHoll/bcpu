# comparators

from bcpu import *

# python code
p2 = 22
p3 = 33
if p2 >= p3:
    p8 = 88
    p9 = 99
else:
    p8 = 8
    p9 = 9

print(p8, p9)

# ---------------- ASM CODE -----------------
# DOING r2 >= r3
def GoE():
    Set(r2, 22)
    Set(r3, 3)

    # else code:
    Set(r8, 8)
    Set(r9, 9)

    # if p2 >= p3
    Sub(r10, r2, r3)

    Set(r11, 88)
    Set(r12, 99)
    Movep(r8, r11, r10) # r8 = 88 if r2 >= r3
    Movep(r9, r12, r10) #r9 = 99 if r2 >= r3
    printr()

# ----------- Method 2 --------------

# DOING r2 < r3
def GoE2():
    # if part:
    Set(r8, 88)
    Set(r9, 99)

    # else part (if p2 < p3)
    Sub(r10, r2, r3)

    # else:
    Set(r11, 8)
    Set(r12, 9)
    Moven(r8, r11, r10) # r8 = 8 if r2 < r3
    Moven(r9, r12, r10) # r9 = 9 if r2 < r3

    printr()
