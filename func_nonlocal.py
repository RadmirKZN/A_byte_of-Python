def funct_outer():
    x = 2
    print ('x равен', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Локалльная х сменилась на х', x)

funct_outer()