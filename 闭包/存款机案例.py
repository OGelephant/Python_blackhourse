def account(amount=0):
    def atm(x,deposit=True):
        nonlocal amount
        if deposit:
            amount = amount +x
            print(amount)
        else:
            amount = amount -x
            print(amount)
    return atm
atm = account()
atm(100)
atm(100)
atm(100)
atm(200,False)