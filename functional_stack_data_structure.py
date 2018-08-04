
__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"


stack_b = [int] * 0  # array of int of size 0 initially


def size_b(an_array: [int]) -> int:
    array_size: int = 0
    for _ in an_array:
        array_size = array_size + 1
    return array_size


stack_j = []


def push_j(value: int) -> [int]:
    global stack_j
    print("push {} into stack {}".format(value, stack_j))
    stack_j = create_a_new_array_j(stack_j, 1)
    stack_j[get_size_j(stack_j) - 1] = value
    print("stack after push is {}".format(stack_j))

def increase_array_size_b(original_array: [int], by_number_of_rows: int) -> [int]:
    original_array_size = size_b(original_array)
    if by_number_of_rows < 1:
        return original_array
    elif original_array_size == 0:
        return [int] * by_number_of_rows
    else:
        new_array = [int] * (original_array_size + by_number_of_rows)
        index = 0
        while index < original_array_size:
            new_array[index] = original_array[index]
            index = index + 1
        return new_array

def pop_j() -> [int]:
    global stack_j
    value = None
    if get_size_j(stack_j) > 0:
        value = stack_j[get_size_j(stack_j) - 1]
        print("pop {} from the stack {}".format(value, stack_j))
        stack_j = create_a_new_array_j(stack_j, -1)
    print("stack after pop is {}".format(stack_j))
    return value

def decrease_array_size_b(original_array: [int], by_number_of_rows: int) -> [int]:
    original_array_size = size_b(original_array)
    if (original_array_size - by_number_of_rows) <= 0:
        return [int] * 0
    else:
        new_array = [int] * (original_array_size - by_number_of_rows)
        index = 0
        while index < size_b(new_array):
            new_array[index] = original_array[index]
            index = index + 1
        return new_array

def get_size_j(array: [int]) -> int:
    i = 0
    for _ in array:
        i = i + 1
    return i

def push_b(value: int):
    global stack_b
    print("pushing {} into stack {}".format(value, stack_b))
    new_stack: [int] = increase_array_size_b(stack_b, 1)
    index: int = (size_b(new_stack) - 1)
    new_stack[index] = value
    stack_b = new_stack
    print("stack after push {}".format(stack_b))

def create_a_new_array_j(old_array: [int], add_number: int) -> [int]:
    new_size = get_size_j(old_array) + add_number
    new_array = [int] * new_size
    if new_size <= 0:
        new_array = []
    elif add_number >= 0:
        for x in range(get_size_j(old_array)):
            new_array[x] = old_array[x]
    elif add_number < 0:
        for x in range(new_size):
            new_array[x] = old_array[x]
    return new_array


def main_j(num_1: int, num_2: int):
    for i in range(num_1):
        push_j(i)
    for j in range(num_2):
        pop_j()
def pop_b() -> int:
    global stack_b
    index = size_b(stack_b) - 1
    result: int = None
    if index >= 0:
        result = stack_b[index]
        print("pop {} from stack {}".format(result, stack_b))
        new_stack = decrease_array_size_b(stack_b, 1)
        stack_b = new_stack
        print("stack after pop {}".format(stack_b))
    return result


def main_b():
    push_b(9)
    push_b(5)
    pop_b()
    pop_b()
    pop_b()
    pop_b()


# start of running code
if __name__ == "__main__":
    pass
