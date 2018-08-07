from object_stack_impl import *

__author__ = "Jieshu Wang"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com"


class Queue(Stack):

    def __init__(self):
        super().__init__(object_type="queue")

    def __str__(self):
        return super().__str__()

    def push(self, value: int, object_type: str="queue"):
        super().push(value, object_type)

    def pop(self) -> Optional[int]:
        value_popped = None
        current_size = self._get_current_size()
        if current_size > 0:
            value_popped = self._get_value_at_index(index=0)
            print("popping {} from queue {}".format(value_popped, self))
            for x in range(1, current_size):
                value = self._get_value_at_index(index=x)
                self._assign_value_to_index(value_to_insert=value, at_index=x-1)
            self._decrease_array_size(by_number_of_rows=1)
            print("queue after pop {}".format(self))
        return value_popped


def main(num_push: int, num_pop: int):
    queue_instance = Queue()

    for i in range(num_push):
        queue_instance.push(i)

    print()

    for _ in range(num_pop):
        value = queue_instance.pop()
        del value  # just remove it from memory, don't really need it

    print()


# start of running code
if __name__ == "__main__":
    main(num_pop=17, num_push=10)
