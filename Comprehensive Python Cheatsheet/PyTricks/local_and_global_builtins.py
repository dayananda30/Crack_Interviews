
global pi
class Test(object):
    a = 'one'
    b = 'two'
    pi = 3.14
    huh = locals()
    c = 'three'

    wow = globals()


    huh['d'] = 'four'
    print huh
    print wow
