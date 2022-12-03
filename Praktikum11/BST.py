#nama       : Sherli Arninda
#NIM        : 24060122120028

class PohonBiner:
    def __init__(self,A,L,R):
        self.A = A
        self.L = L
        self.R = R

def MakePB(A,L,R):
    return [A,L,R]

def Akar(P):
    return P[0]

def Left(P):
    return P[1]

def Right(P):
    return P[2]

def IsTreeEmpty(P):
    if P==None:
        return True
    else:
        return False

def IsBiner(P):
    if not IsTreeEmpty and not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P)):
        return True
    else:
        return False

def IsOneElmt(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
        return True
    else:
        return False

def IsUnerRight(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P)):
        return True
    else:
        return False

def IsUnerLeft(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and IsTreeEmpty(P):
        return True
    else:
        return False

def NbElmt(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmt(P):
        return 1
    else:
        return 1 + NbElmt(Left(P)) + NbElmt(Right(P))

def IsSkewRight(P):
    if IsUnerRight(P):
        if IsOneElmt(Right(P)):
            return True
        else:
            return IsSkewRight(Right(P))
    else:
        return False

def IsSkewLeft(P):
    if IsUnerLeft(P):
        if IsOneElmt(Left(P)):
            return True
        else:
            return IsSkewLeft(Left(P))
    else:
        return False

def is_member(P,X:int):
    if IsTreeEmpty(P):
        return False
    else:
        if Akar(P) == X:
            return True
        else:
            if IsBiner(P):
                return is_member(Left(P), X) or is_member(Right(P), X)
            elif IsUnerLeft(P):
                return is_member(Left(P), X)
            elif IsUnerRight(P):
                return is_member(Right(P), X)
            else:
                return False

def level_of_X(P, X):
    if not is_member(P, X):
        return 0
    else:
        if Akar(P) == X:
            return 1
        else:
            if IsBiner(P):
                return 1 + level_of_X(Left(P), X) + level_of_X(Right(P), X)
            elif IsUnerLeft(P):
                return 1 + level_of_X(Left(P), X)
            elif IsUnerRight(P):
                return 1 + level_of_X(Right(P), X)

def TinggiPohon(P):
    if IsTreeEmpty(P):
        return 0
    else:
        if NbElmt(Left(P))>NbElmt(Right(P)):
            return 1+TinggiPohon(Left(P))
        else:
            return 1+TinggiPohon(Right(P))

PB=MakePB(3,
            MakePB(1,
                MakePB(3,None,None),
                None),
            MakePB(2,None,None))
print("P = ",PB)
print("TinggiPohon(P) = ",TinggiPohon(PB))