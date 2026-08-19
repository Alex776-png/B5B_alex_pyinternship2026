count = 0

def call_counter():
    global count
    count += 1

call_counter()
call_counter()
call_counter()
call_counter()

print("Final count:", count)