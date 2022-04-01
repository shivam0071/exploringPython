import multiprocessing


def run(array):
    array[0] += 1
    array[1] += 1
    print(f"ID inside thread:{id(array)}")

if __name__ == "__main__":

    # The first attribute is the datatype in the list.
    var = multiprocessing.Array("i", [0, 1])
    print(f"ID outside thread:{id(var)}")

    process1 = multiprocessing.Process(target=run, args=[var])
    process1.start()
    process1.join()

    print("the original var is [0, 1]")
    print(f"the updated var is {list(var)}")