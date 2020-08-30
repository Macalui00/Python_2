from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Acá estan los args: ", args)
        print("Acá estan los kwargs: ", kwargs)
        return fn(*args, **kwargs)
    return wrapper

@show_args
def suma(x, y):
    return x + y 

print(suma(8,9))