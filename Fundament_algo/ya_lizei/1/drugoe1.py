import sys
from decimal import Decimal, getcontext

getcontext().prec = 50

a, b, c, v0, v1, v2 = map(Decimal, input().split())

# All possible strategies
t1 = a/v0 + c/v1 + b/v2  # H->S->P->H
t2 = b/v0 + c/v1 + a/v2  # H->P->S->H
t3 = a/v0 + a/v1 + b/v0 + b/v1  # H->S->H->P->H
t4 = b/v0 + b/v1 + a/v0 + a/v1  # H->P->H->S->H

# Additional routes considering going back
t5 = a/v0 + c/v1 + c/v2 + a/v2  # H->S->P->S->H
t6 = b/v0 + c/v1 + c/v2 + b/v2  # H->P->S->P->H
t7 = a/v0 + c/v1 + b/v2 + a/v0 + a/v1  # H->S->P->H->S->H
t8 = b/v0 + c/v1 + a/v2 + b/v0 + b/v1  # H->P->S->H->P->H

answer = min(t1, t2, t3, t4, t5, t6, t7, t8)
print(f"{answer:.15f}")
