def cero():
    return 'cero'

def uno():
    return 'uno'

def indirect(i):
    switcher = {
        0:zero,
        1:one,
        2:lambda:'two'
    }
    func=switcher.get(i, lambda : 'invalid')
    return func()

indirect(0)