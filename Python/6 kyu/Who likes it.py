# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return str(names[0]+' likes this')
    elif len(names) == 2:
        return str(names[0]+' and '+names[1]+' like this')
    elif len(names) == 3:
        return str(names[0]+', '+names[1]+' and '+names[2]+' like this')
    else:
        return str(names[0]+', '+names[1]+' and '+str(len(names)-2)+' others like this')

print(likes([]))
print(likes(['Jane']))
print(likes(['Jane','Julie']))
print(likes(['Jane','Julie','Dana']))
print(likes(['Jane','Julie','Dana','Kate']))

#--------------- Best Practice -----------------------

def likes2(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)

#--------------- Best Practice -----------------------

def likes3(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

#--------------- Best Practice -----------------------

def likes4(names):
    namez=names[:]
    msg=['no one likes this','{0} likes this','{0} and {1} like this','{0}, {1} and {2} like this','{0}, {1} and {remains} others like this']
    return msg[min(4,len(namez))].format(*namez,remains=len(namez)-2)
