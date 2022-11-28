import ast

def is_empty_LoL(S):
    return S == []

def is_atom(S):
    return len(str(S)) == 1

def is_List(S):
    return not(is_atom(S))

def FirstElmt(S):
    return S[0]

def tail_List(S):
    if not(is_empty_LoL(S)):
        return S[1:]

def JumlahKartu(S):
    if is_empty_LoL(S):
        return 0
    elif is_List(FirstElmt(S)):
        return JumlahKartu(FirstElmt(S)) + JumlahKartu(tail_List(S))
    else:
        return 1 + JumlahKartu(tail_List(S))

i = ast.literal_eval(input())
print(JumlahKartu(i))
