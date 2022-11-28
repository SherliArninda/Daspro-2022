import ast
list_of_list = ast.literal_eval(input())

def is_empty_LoL(S):
    return S==[]

def first_List(S):
    if not(is_empty_LoL(S)):
        return S[0]

def tail_List(S):
    if not(is_empty_LoL(S)):
        return S[1:]

def nbElmtList(S):
    if isinstance(S, list):
        if is_empty_LoL(S):
            return 0
        else:
            return 1 + nbElmtList(tail_List(S))
    else:
        return 1

def isOneElmt(S):
    return nbElmtList(S) == 1

def konso_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return [L]+S

def Max2(a,b):
    if a>=b:
        return a
    else:
        return b

def Max(L):
    if isOneElmt(L):
        return first_List(L)
    else : 
        if isinstance(first_List(L),int):
            if isinstance(first_List(tail_List(L)),int):
                return Max(konso_LoL(Max2(first_List(L), first_List(tail_List(L))), tail_List(tail_List(L))))
            else:
                return Max(konso_LoL(first_List(L), tail_List(tail_List(L))))
        else :
            return Max(tail_List(tail_List(L)))


def UtangNegara(L, maks=Max(list_of_list)):
    if is_empty_LoL (L):
        return maks
    else: 
        if isinstance(first_List(L),int):
            return UtangNegara(tail_List(L))
        else :
            return Max(first_List(L)) + UtangNegara(tail_List(L))


print(UtangNegara(list_of_list)* 1000000)