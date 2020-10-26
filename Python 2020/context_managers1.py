import time
from contextlib import contextmanager

def looper(n):
    ls = []
    for i in range(n):
        ls.append(i*i)

# Class Based Manager implementing the enter and exit dunders
class ContectManagerExample():

    def __init__(self):
        self.time = None

    def __enter__(self):
        print("Entering the Context")
        self.time = time.time()


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the Context")
        print(f"Time Taken {time.time() - self.time} sec")


@contextmanager
def function_based_manager(n):
    try:
        print("Entering the function based context")  # WE can add a code to open file, hold thread here
        time1 = time.time()
        yield looper(n)
    finally:
        print("Exiting the Funciton Based Context")
        print(f"Time Taken {time.time() - time1} sec")


# Another Simple
@contextmanager
def anotherfunctionbased(name):
    try:
        f = open(name, "w")
        yield f
    finally:
        f.close()


if __name__ == "__main__":
    with ContectManagerExample() as timer:
        looper(100000)

    with function_based_manager(100000) as timer2:
        pass

