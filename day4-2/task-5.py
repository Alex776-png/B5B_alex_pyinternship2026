mode = "global"

def outer():
    mode = "outer"

    def inner():
        mode = "inner"
        print("Inside inner:", mode)

    print("Inside outer:", mode)
    inner()
    print("Back inside outer:", mode)


print("Global:", mode)
outer()
print("Global again:", mode)