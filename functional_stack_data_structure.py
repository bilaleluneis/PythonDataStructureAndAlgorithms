
__author__ = "Jieshu Wang"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com"


stack_j = []


def push_j(value: int) -> [int]:
    global stack_j
    print("push {} into stack {}".format(value, stack_j))
    stack_j = create_a_new_array_j(stack_j, 1)
    stack_j[get_size_j(stack_j) - 1] = value
    print("stack after push is {}".format(stack_j))


def pop_j() -> [int]:
    global stack_j
    value = None
    if get_size_j(stack_j) > 0:
        value = stack_j[get_size_j(stack_j) - 1]
        print("pop {} from the stack {}".format(value, stack_j))
        stack_j = create_a_new_array_j(stack_j, -1)
    print("stack after pop is {}".format(stack_j))
    return value


def get_size_j(array: [int]) -> int:
    i = 0
    for _ in array:
        i = i + 1
    return i


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


# start of running code
if __name__ == "__main__":
    main_j(2, 4)