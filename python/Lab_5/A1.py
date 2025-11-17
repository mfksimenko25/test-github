def textplase(st):
    p = st.find("(")
    while (p!=-1):
        pl = st.find("(", p+1)
        pr = st.find(")", p+1)
        if (pl == -1 or pr < pl):
            st = st[:p] + st[pr+1:]
            p = st.find("(")
        else:
            p = pl
        #p = -1
    return st
print(textplase(' Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему недождь) () (())'))




