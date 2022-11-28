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

def FirstElmt(S):
    return S[0]

def jumlahPermen(L):
    if is_empty_LoL(L):
        return 0
    elif isinstance(first_List(L), int):
        return FirstElmt(L) + jumlahPermen(tail_List(L))
    else:
        return jumlahPermen(first_List(L)) + jumlahPermen(tail_List(L))

def totalBiaya(L):
    if is_empty_LoL(L):
        return 0
    else:
        if isinstance(first_List(L), int):
            if FirstElmt(L)%2==0:
                return FirstElmt(L)*4000 + totalBiaya(tail_List(L))
            elif FirstElmt(L)%2!=0:
                return FirstElmt(L)*3000 + totalBiaya(tail_List(L))
        else:
            if jumlahPermen(first_List(L)) % 2 == 0:
                return jumlahPermen(first_List(L))*2000 + totalBiaya(tail_List(L))
            elif jumlahPermen(first_List(L)) % 2 != 0:
                return jumlahPermen(first_List(L))*1000 + totalBiaya(tail_List(L))

i = ast.literal_eval(input())
print(totalBiaya(i))