__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Oct 2019"
__email__ = "bilaleluneis@gmail.com, foundwonder@gmail.com"

from unittest import TestCase

from LSP import Number, Integer
from generic_operation import BinaryOperation, UnaryOperation
from simple_calculator import CalculatorProtocol, SimpleCalculator, Operations
from vector import VectorInterface, CPUVector


# noinspection PyCallByClass
class TestSimpleCalculator(TestCase):

    def setUp(self) -> None:
        self.__supported_operations: Operations = {
            "+": BinaryOperation("+", lambda x, y: x + y),
            "-": BinaryOperation("-", lambda x, y: x - y),
            "*": BinaryOperation("*", lambda x, y: x * y),
            "/": BinaryOperation("/", lambda x, y: x / y),
            "**": BinaryOperation("**", lambda x, y: x ** y),
            "sqr": UnaryOperation("sqr", lambda x: x ** 2),
            "sqr root": UnaryOperation("sqr root", lambda x: x ** 0.5),
            "%": BinaryOperation("%", lambda x, y: x % y),
            "mean": BinaryOperation("mean", lambda x, y: (x + y) / 2)
        }

    def test_init_calculator(self) -> None:
        simple_calculator: CalculatorProtocol[int] = SimpleCalculator[int](self.__supported_operations)
        simple_calculator.operator('+')

    def test_all_clear(self) -> None:
        calculator: CalculatorProtocol[int] = SimpleCalculator[int](self.__supported_operations)
        calculator.operand(1)
        calculator.operator('+')
        calculator.operand(3)
        calculator.evaluate()
        self.assertTrue(calculator.accumulator is not None)
        calculator.clear()
        self.assertTrue(calculator.accumulator is None)

    def test_single_int_plus(self) -> None:
        simple_calculator: CalculatorProtocol[int] = SimpleCalculator[int](self.__supported_operations)
        simple_calculator.operand(1)
        simple_calculator.operator('/')
        simple_calculator.operand(2)
        simple_calculator.evaluate()
        self.assertEqual(simple_calculator.accumulator, 0.5)

    def test_multiple_int_operators(self) -> None:
        calculator: CalculatorProtocol[int] = SimpleCalculator[int](self.__supported_operations)
        calculator.operand(1)
        calculator.operator("+")
        calculator.operand(2)
        calculator.operator('/')
        calculator.operand(3)
        calculator.operator('*')
        calculator.operand(5)
        calculator.evaluate()  # ((1+2)/3)*5 = 5
        self.assertEqual(calculator.accumulator, 5)

    def test_custom_integer_calculator(self) -> None:
        calculator: CalculatorProtocol[Number[int]] = SimpleCalculator[Integer](self.__supported_operations)
        calculator.operand(Integer(1))
        calculator.operator('+')
        calculator.operand(Integer(2))
        calculator.evaluate()
        self.assertEqual(calculator.accumulator.value, 3)

    def test_custom_vector_calculator(self) -> None:
        vector_calculator: CalculatorProtocol[VectorInterface[int]] = SimpleCalculator[CPUVector[int]](
            self.__supported_operations)
        vector_calculator.operand(CPUVector([1, 2, 3]))
        vector_calculator.operator('+')
        vector_calculator.operand(CPUVector([2, 5, 4]))
        vector_calculator.evaluate()
        self.assertEqual(vector_calculator.accumulator.value, [3, 7, 7])

    def tearDown(self) -> None:
        del self.__supported_operations
