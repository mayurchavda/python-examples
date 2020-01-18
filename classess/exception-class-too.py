class B:
    pass
class C(B):
    pass
class D(C):
    pass

for a in [B, C, D]:
    try:
        raise a()
    except D:
        print("dD")
    except C:
        print("cC")
    except B:
        print("bB")
