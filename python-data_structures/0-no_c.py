def no_c(my_string):
    bb = my_string
    aa = list(bb)
    for i in range(len(aa) - 2):
        if aa[i] == "c":
            del aa[i]
        elif aa[i] == "C":
            del aa[i]

    ss = "".join(aa)
    return ss


x = "C is fun!"
y = no_c(x)
print(y)
