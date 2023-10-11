from prindent import prindent

# Example usage
prindent('first loop')
for i in range(2):
    prindent('i:', i)
    prindent('second loop')
    for j in range(2):
        prindent('j:', j)
        if j == 1:
            prindent('j=1')

if True:
    if True:
        for i in range(2):
            prindent('Custom indent', indent='---> ')
