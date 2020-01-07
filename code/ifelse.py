# if else
from bcpu import *

# python
def pythonIfElse():
    p2 = 2
    p3 = 3
    # goto else when p2 <= 0
    if(p2 > 0):
        p3 += 3
        # goto endif
    else:
        p3 += 1
    #endif


    # expect p2 =2, p3 = 6
    print(p2,p3)

pythonIfElse()

# assembly
ifelse = """
Set(r2,2)
Set(r3,3)
# if r2 > 0
# goto else when r2 <= 0
Set(r0, 0)
Sub(r9, r0, r2)         # bigger - smaller

Addi(r10, pc, ?else)    #addr of else
Movep(pc, r10, r9)      #goto endif if r2 <= 0
    # if part
    Addi(r3, r3, 3)
    # goto endif (unconditionally)
    Addi(pc, pc, ?endif)

    #>else part
    Addi(r3, r3, 1)

#>endif
"""
# print and start function calls are OS codes and happen outside of the """ """
start(ifelse)
printr()
printm()
