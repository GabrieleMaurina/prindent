from prindent import prindent

# auto indentation usage
prindent('first loop')
for i in range(2):
    prindent('i:', i)
    prindent('second loop')
    for j in range(2):
        prindent('j:', j)
        if j == 1:
            prindent('j=1')

# custom string for indentation
if True:
    if True:
        for i in range(2):
            prindent('Custom indent', indent='---> ')

# multiple newlines
if True:
    prindent('String\nwith\nnewline')

# multiple args and kwargs
if True:
    prindent('first', 'second', end='$')
