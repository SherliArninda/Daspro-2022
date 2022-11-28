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

def isPrima(S, i=2):
    if (S<2):
        return False
    elif (S==2):
        return True
    elif (S % 2 == 0):
        return False
    elif (i * i > S):
        return True
    else:
        return isPrima(S, i+1)

def penjumlahanPrima(S):
    if is_empty_LoL(S):
        return 0
    elif isinstance(first_List(S),int):
        if isPrima(FirstElmt(S)):
            return FirstElmt(S) + penjumlahanPrima(tail_List(S))
        else:
            return penjumlahanPrima(tail_List(S))
    else:
        return penjumlahanPrima(first_List(S)) + penjumlahanPrima(tail_List(S))

i = ast.literal_eval(input())
print(penjumlahanPrima(i))