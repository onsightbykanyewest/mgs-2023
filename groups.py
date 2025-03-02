def isClosed(q,op):
    return all(op(x,y) in q
                for x in q
                for y in q)

def isMonoid(q,op):
    raise NotImplemented

def findIdentity(q,op):
    for x in q:
        if all(op(x,y) == y and op(y,x) == y for y in q):
            return x
    return False

def findInverse(x,q):
    e = findIdentity(q,op)
    if e is False:
        return False
    else:
        for y in q:
            if op(y,x) == e:
                return y
        #this line cannot be reached
def hasInverses(q,op):
    return all(findInverse(x) for x in q)

def isGroup(q,op):
    #raise NotImplemented
    return isMonoid(q,op) and hasInverses(q,op)

q1 = {0,1,2,3,4,5,6}
q2 = {1,2,3,4,5,6}

def mult(a,b):
    return (a*b) % 7


print(isGroup(q1,mult))
print(isGroup(q2,mult))

