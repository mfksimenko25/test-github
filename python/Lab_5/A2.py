import re

def checksent(st):
    return  re.split(r'(?<=[.?!]) ', st)
for l in checksent(' He jests at scars. That never felt a wound! Hello, friend! Are you OK?'):
    print(l.strip())










