# pylint: disable=missing-module-docstring    # чтобы не быть Капитаном Очевидностью
# pylint: disable=missing-class-docstring     # чтобы не быть Капитаном Очевидностью
# pylint: disable=missing-function-docstring  # чтобы не быть Капитаном Очевидностью
# pylint: disable=line-too-long               # строки с ожидаемым выводом

import unittest
from circuit import CircuitComponent, CircuitWire


class CircuitWireTests(unittest.TestCase):
    def test_SetZeroValue_Calculated(self):
        wire = CircuitWire()

        wire.set(0)

        self.assertEqual(wire.value, 0)

    def test_SetPositiveValue_Calculated(self):
        wire = CircuitWire()

        wire.set(5)

        self.assertEqual(wire.value, 5)

    def test_GetValueAfterInitialize_ReturnZero(self):
        wire = CircuitWire()

        self.assertEqual(wire.get(), 0)

    def test_GetValueAfterAssignment_ReturnAssignment(self):
        wire = CircuitWire()

        wire.value = 5

        self.assertEqual(wire.get(), 5)


class CircuitComponentTests(unittest.TestCase):
    def test_AttachUndefinedWireOnDefinedRegister_AssertThrown(self):
        component = CircuitComponent(['In'])
        wire = None

        with self.assertRaises(AssertionError):
            component.attach('In', wire)

    def test_AttachDefinedWireOnUndefinedRegister_AssertThrown(self):
        component = CircuitComponent([])
        wire = CircuitWire()

        with self.assertRaises(AssertionError):
            component.attach('In', wire)

    def test_AttachDefinedWireOnDefinedRegister_Calculate(self):
        component = CircuitComponent(['In'])
        wire = CircuitWire()

        component.attach('In', wire)

        self.assertEqual(component.get_register('In'), 0)

    def test_SetUndefinedRegister_AssertThrown(self):
        component = CircuitComponent([])

        with self.assertRaises(AssertionError):
            component.set_register('In', 5)

    def test_SetDefinedNotConnectedRegister_Calculate(self):
        component = CircuitComponent(['In'])

        component.set_register('In', 5)

        self.assertEqual(component.registers['In'], 5)

    def test_SetDefinedConnectedRegister_CalculateAndFillWire(self):
        component = CircuitComponent(['In'])
        wire = CircuitWire()

        component.attach('In', wire)
        component.set_register('In', 5)

        self.assertEqual(component.registers['In'], 5)
        self.assertEqual(wire.get(), 5)

    def test_GetUndefinedRegister_AssertThrown(self):
        component = CircuitComponent([])

        with self.assertRaises(AssertionError):
            component.get_register('In')

    def test_GetDefinedRegister_Calculate(self):
        component = CircuitComponent(['In'])

        component.registers['In'] = 5

        self.assertEqual(component.get_register('In'), 5)

    def test_Update_RecieveWireValues(self):
        component = CircuitComponent(['In'])
        wire = CircuitWire()

        component.attach('In', wire)
        wire.set(5)
        component.update()

        self.assertEqual(component.get_register('In'), 5)


if __name__ == '__main__':
    unittest.main()
