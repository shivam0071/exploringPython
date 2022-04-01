import concurrent.futures


def run(array):
    array[0] += 1
    array[1] += 1
    print(f"ID inside thread:{id(array)}")

var = [0, 1]
print(f"ID outside thread:{id(var)}")
with concurrent.futures.ThreadPoolExecutor() as executor:
    err_detect = executor.submit(run, var)

print("the original var is [0, 1]")
print(f"the updated var is {var}")