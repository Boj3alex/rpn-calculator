import unittest
from io import StringIO
from unittest.mock import patch
from app.evaluation import rpn_evaluation


class RPNNotationCalculatorTests(unittest.TestCase):

    def test_no_input(self):
        self.assertEqual(rpn_evaluation(''), 0)

    def test_simple_addition(self):
        self.assertEqual(rpn_evaluation('2 3 +'), 5)

    def test_simple_division(self):
        self.assertEqual(rpn_evaluation('5 2 /'), 2)

    def test_multiplication_and_addition(self):
        self.assertEqual(rpn_evaluation('4 7 + 2 *'), 22)

    def test_multiplication_and_addition_complex(self):
        self.assertEqual(rpn_evaluation('2 3 * 11 14 * +'), 160)

    def test_modulo_and_multiplication(self):
        self.assertEqual(rpn_evaluation('8 4 % 10 +'), 10)

    def test_invalid_operator(self):
        with self.assertRaises(Exception) as details:
            rpn_evaluation('30 13 &')
        self.assertTrue('Invalid character' in str(details.exception))

    def test_invalid_operand(self):
        with self.assertRaises(Exception) as details:
            rpn_evaluation('25 10 * 4 t + +')
        self.assertTrue('Invalid character' in str(details.exception))

    def test_floating_point_numbers(self):
        with self.assertRaises(Exception) as details:
            rpn_evaluation('23 4.5 + 3 *')
        self.assertTrue('Floating-point numbers are not accepted.' in str(details.exception))

    def test_invalid_expressions(self):
        with patch('sys.stdout', new=StringIO()) as output_buffer:
            rpn_evaluation('365 *')
        self.assertEqual(output_buffer.getvalue(), 'Invalid RPN expression\n')


if __name__ == '__main__':
    unittest.main()
