import random
import sys
from time import perf_counter


my_awesome_list = list()
INTERVAL = 10**7

begin_list = perf_counter()
for x in range(0, INTERVAL):
    my_awesome_list.append(random.randint(0, 3))
print(f"Total time (to create list): {perf_counter() - begin_list}seg | sizeof: {sys.getsizeof(my_awesome_list)} bytes")

def number_generate():
    for _ in range(0, INTERVAL):
        yield random.randint(0, 3)

begin_generate = perf_counter()
my_awesome_generate = number_generate()
print(f"Total time (to create generate): {perf_counter() - begin_generate}seg | sizeof: {sys.getsizeof(my_awesome_generate)} bytes")

def with_out_yield():
    my_dict = dict()
    new_list = list()
    
    # O(n) -> for item in my_awesome_list
    for item in my_awesome_list:
        if item not in my_dict.keys():
            my_dict[item] = 1
        else:
            my_dict[item] += 1

    # O(n) k, v in dict.items()
    for k, v in my_dict.items():
        if v > 1:
            new_list.append((k, v))
 
    # O(n) * O(n) = O(nˆ2)
    return new_list

def dict_generate(my_dict: dict):
    for k, v in my_dict.items():
        yield k, v

def with_yield():
    my_dict = dict()
    new_list = list()

    for number in my_awesome_generate:
        if number not in my_dict.keys():
            my_dict[number] = 1
        else:
            my_dict[number] += 1
    
    for k, v in dict_generate(my_dict=my_dict):
        if v > 1:
            new_list.append((k, v))

    return new_list

def main():
    start = perf_counter()
    result = with_out_yield()
    print(f"Total time (with_out_yield): {perf_counter() - start}seg | sizeof: {sys.getsizeof(result)} bytes")

    start = perf_counter()
    result = with_yield()
    print(f"Total time (with_yield): {perf_counter() - start}seg | sizeof: {sys.getsizeof(result)} bytes")


if __name__ == "__main__":
    main()