def PisanoPeriod(m):
    current = 0
    next = 1
    period = 0
    while True:
        oldNext = next
        next = (current + next) % m
        current = oldNext
        period = period + 1
        if current == 0 and next == 1:
            return period
print(PisanoPeriod(150))

