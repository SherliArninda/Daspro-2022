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

def penjumlahanGanjil(S):
    if is_empty_LoL(S):
        return 0
    elif is_List(first_List(S)):
        return penjumlahanGanjil(FirstElmt(S)) + penjumlahanGanjil(tail_List(S))
    else:
        if FirstElmt(S) %2 !=0:
            return FirstElmt(S) + penjumlahanGanjil(tail_List(S))
        else:
            return penjumlahanGanjil(tail_List(S))

i = ast.literal_eval(input())
print(penjumlahanGanjil(i))