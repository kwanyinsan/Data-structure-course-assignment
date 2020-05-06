from queuem import *
from listm import *

def jose(n, m):
    if n <= 1:
        print("Can't create cicle, n is not > 1")
    else:
        c = List()
        for i in range(1, n + 1):
            insert(c, i, i)
    if m <= 0 :
        print("Can't eliminate people, m is not > 0")
    else:
        deadc = Queue()
        p = 2
        for i in range(0, n):
            for i in range(0, m):
                while (p > length(c)):
                    p = p - length(c)
                dead = get(c, p)
                p = p + 1
            x = locatebyvalue(c, dead)
            delete (c, x)
            p = x
            enqueue(deadc, dead)
    displayq(deadc)