"""
def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec

def who_is_harry():
    print("Prahalad is a good boy")

who_is_harry=dec1(who_is_harry)
who_is_harry()
"""


def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")

    return nowexec

@dec1
def who_is_harry():
    print("Prahalad is a good boy")



who_is_harry()