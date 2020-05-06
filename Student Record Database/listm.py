class List:
    def __init__(self, extlist=None):
        if extlist is None:
                    self.inlist = []
        else:
            self.inlist = extlist


def length(L):
    return len(L.inlist)


def isempty(L):
    if len(L.inlist)==0:
        return True
    else:
        return False

def get(L, i):
    if isempty(L):
        print("The get() is unsuccessful!")
        print("The list is empty!")
        return -1
    elif (i<1) or (i>length(L)):
        return -1
    else:
        return(L.inlist[i-1])

def locatebyvalue(L, x):
    position = 1
    for item in L.inlist:
        if x == item:
            return position
        else:
            position = position+1
    return -1        

def locatebyid(L, idd):
    position = 1
    for item in L.inlist:
        if item.id == idd:
            return position
        else:
            position = position+1
    return -1        

def insert(L, i, x):
    if (i<1) or (i>length(L)+1):
        print("The insert() is unsuccessful!")
        print("The index given is out of range!")
        
    else: 
        L.inlist.insert(i-1, x)

def delete(L, i):
    if isempty(L):
        print("The delete() is unsuccessful!")
        print("The list is empty!")
        return
    elif (i<1) or (i>length(L)):
        #print("The delete() is unsuccessful!")
        #print("The index given is out of range!")
        return
    else: 
        del L.inlist[i-1]


def display(L):
    print(L.inlist)



    
