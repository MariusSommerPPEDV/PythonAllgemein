# Namespace & Scope Beispiel

x = "Global"


def f():
    x: str = "enlcosing"

    def g():
        x ="local"
        print(x)

    g()
    print(x)


f()
print(globals())
