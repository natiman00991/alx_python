def no_c(my_string):
    bb = my_string
    aa = list(bb)
    new_aa = []
    for char in aa:
        if char not in ["c", "C"]:
            new_aa.append(char)
    ss = "".join(new_aa)
    return ss
