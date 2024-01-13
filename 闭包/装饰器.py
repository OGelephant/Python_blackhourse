def outer( func):
    def inner ():
        print(" I will sleep!")
        func()
        print(" I am get up now!")
    return inner

@outer
def sleep ():
    import random
    import time
    print("sleeping now!")
    time.sleep(random.randint(1,5))

sleep()