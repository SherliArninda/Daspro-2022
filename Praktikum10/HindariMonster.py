import ast

def is_empty_LoL(S):
    return S==[]

def is_atom(S):
    return len(str(S)) == 1

def is_List(S):
    return not(is_atom(S))

def first_List(S):
    if not(is_empty_LoL(S)):
        return S[0]

def tail_List(S):
    return S[1:]

def konso_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return [L]+S

def FirstElmt(S):
    return S[0]

def Rember(a,S):
    if is_empty_LoL(S):
        return S
    else :
        if is_List(first_List(S)):
            return konso_LoL(Rember(a,first_List(S)),Rember(a,tail_List(S)))
        else :
            if FirstElmt(S) == a:
                return Rember(a,tail_List(S))
            else :
                return konso_LoL(FirstElmt(S), Rember(a,tail_List(S)))

def CekMonster(a,S):
    if is_empty_LoL(S):
        return S
    else :
        if is_List(first_List(S)):
            return konso_LoL(CekMonster(a,first_List(S)), CekMonster(a,tail_List(S)))
        else :
            if FirstElmt(S) % a == 0:
                return CekMonster(a,Rember(a,tail_List(S)))
            else :
                return konso_LoL(FirstElmt(S), CekMonster(a,tail_List(S)))

list_of_list = ast.literal_eval(input())
i = int(input())
print(CekMonster(2,list_of_list))