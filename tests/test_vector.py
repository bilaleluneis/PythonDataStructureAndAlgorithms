__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2020"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from typing import Type
from unittest import TestCase
from vector import VectorInterface, CPUVector, GPUVector, vector


class TestVector(TestCase):

    def test_init_interface(self) -> None:
        with self.assertRaises(TypeError):
            vector_interface = VectorInterface[int]([1, 2])  # type: ignore

    def test_init_concrete_class(self) -> None:
        cpu_vector: VectorInterface[int] = CPUVector[int]()
        gpu_vector: VectorInterface[float] = GPUVector[float]()
        self.assertEqual(len(cpu_vector), 0)
        self.assertEqual(len(gpu_vector), 0)

    def test_add_vector(self) -> None:
        cpu_vector_1: VectorInterface[int] = CPUVector[int]([1, 2, 3])
        cpu_vector_2: VectorInterface[int] = CPUVector[int]([2, 4, 5])
        sum_cpu_vector = cpu_vector_1 + cpu_vector_2
        self.assertEqual(sum_cpu_vector.value, [3, 6, 8])

        gpu_vector_1: VectorInterface[float] = GPUVector[float]([1.0, 2.2, 3.5])
        gpu_vector_2: VectorInterface[float] = GPUVector[float]([2, 4.3, 5.4])
        sum_gpu_vector = gpu_vector_1 + gpu_vector_2
        self.assertEqual(sum_gpu_vector.value, [3.0, 6.5, 8.9])

    def test_add_different_subtype(self) -> None:
        cpu_vector_3: VectorInterface[int] = CPUVector[int]([1, 2, 3])
        gpu_vector_3: VectorInterface[int] = GPUVector[int]([1, 2, 3])
        with self.assertRaises(AttributeError):
            vector_sum = cpu_vector_3 + gpu_vector_3

    def test_init_function(self) -> None:
        vector_type: Type[VectorInterface[int]] = vector(int)
        v = vector_type([1, 2])
        self.assertTrue(hasattr(v, 'is_cpu'))





