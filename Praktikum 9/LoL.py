#Nama    : Sherli Arninda
#NIM     : 24060122120028


def jml_elemen_list(S):
    if isinstance(S,list):
        return len (S)
    else:
        return 1

def is_empty_LoL(S):
    return S==[]

def is_atom(S):
    return not(is_empty_LoL(S)) and jml_elemen_list(S)==1

def is_List(S):
    return not(is_atom(S))

def konso_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return [L]+S

def konsi_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return S+[L]

def first_List(S):
    if not(is_empty_LoL(S)):
        return S[0]

def tail_List(S):
    if not(is_empty_LoL(S)):
        return S[1:]

def last_List(S):
    if not (is_empty_LoL(S)):
        return S[-1:]

def head_List(S):
    if not(is_empty_LoL(S)):
        return S[:-1]

def FirstElmt(S):
    return S[0]

def IsOneElmt(S):
    return jml_elemen_list(S) == 1


print("Contoh 1")
def IsEqs(S1,S2):
    if is_empty_LoL(S1) and is_empty_LoL(S2):
        return True
    elif not(is_empty_LoL(S1)) and is_empty_LoL(S2):
        return False
    elif is_empty_LoL(S1) and not(is_empty_LoL(S2)):
        return False
    else:
        if is_atom(first_List(S1)) and is_atom(first_List(S2)):
            return first_List(S1)==first_List(S2) and IsEqs(tail_List(S1), tail_List(S2))
        elif is_List(first_List(S1)) and is_List(first_List(S2)):
            return IsEqs(first_List(S1), first_List(S2)) and IsEqs(tail_List(S1), tail_List(S2))
        else:
            return False
L1 = ['a',['b','c','e']]
L2 = ['a',['b','c']]
print(IsEqs(L1,L2))

print("============")
print("Contoh 2")
def IsMemberS(A,S):
    if is_empty_LoL(S):
        return False
    else:
        if is_atom(first_List(S)):
            return A==first_List(S)
        elif is_List(first_List(S)):
            return IsMemberS(A, first_List(S)) or IsMemberS(A, tail_List(S))
        else :
            return False
A = 'a'
L = ['a',['b','c','e']]
print(IsMemberS(A,L))

print("============")
print("Contoh 3")
def IsMemberLS(L,S):
    if is_empty_LoL(L) and is_empty_LoL(S):
        return True
    elif not is_empty_LoL(L) and not is_empty_LoL(S):
        if (is_atom(first_List(S))):
            return IsMemberLS(tail_List(L,S))
        else:
            if IsEqs(L, first_List(S)):
                return True
            else:
                return IsMemberLS(L, tail_List(S))

L = [2,3]
S = [1,[2,3],4]
print(IsMemberLS(L,tail_List(S)))

print("============")
print("Contoh 4")

def Rember(a,S):
    if is_empty_LoL(S):
        return S
    elif is_List(first_List(S)):
        return konso_LoL(first_List(S),Rember(a,tail_List(S)))
    else:
        if FirstElmt(S)==a:
            return Rember (a,tail_List(S))
        else:
            return konso_LoL(FirstElmt(S),Rember(a,tail_List(S)))

a = 3
S = [1,2,3,6,7]
print(Rember(a,S))

print("============")
print("Contoh 5")

def Max2(a,b):
    if a>=b:
        return a
    else:
        return b

def Max(S):
    if IsOneElmt(S):
        if is_atom(first_List(S)):
            return first_List(S)
        else:
            return Max(first_List(S))
    else:
        if is_atom(first_List(S)):
            return Max2(first_List(S),Max(tail_List(S)))
        else:
            return Max2(Max(first_List(S)),Max(tail_List(S)))

S = [11,12,13,14,15]
print(Max(S))
