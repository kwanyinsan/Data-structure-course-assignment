from listm import *


class Queue(List):
    def __init__(self, que=None):
        List.__init__(self, que)
        self.rear = length(self)


def isemptyq(q):
    if isempty(q):
        return True
    else:
        return False

def enqueue(q, x):
    q.rear= q.rear + 1
    insert(q, q.rear, x)
    


def dequeue(q):
    if isemptyq(q):
        print("Dequeue error, queue underflow!!!\n")
        return -1
    else:
        tmp = get(q, 1)
        delete(q, 1)
        q.rear = q.rear - 1
        return tmp    



def getfront(q):
    if isemptyq(q):
        print("Getfront error, queue underflow!!!\n")
        return -1
    else:
        tmp = get(q, 1)
        return tmp


def displayq(q):
    display(q)




