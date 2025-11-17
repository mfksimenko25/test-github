def abbr(st):
    sarr = st.split()
    ab = ""
    for s in sarr:
        if len(s)>=3:
            ab += s[0].upper()
    return ab
print(abbr("New York City"))

