import re

floating_point_regex = '[0-9]*\.[0-9]*'

def do_operation(element1, element2, operator):
    if operator == '+':
        return element1 + element2
    if operator == '-':
        return element1 - element2
    if operator == '*':
        return element1 * element2
    if operator == '/':
        return int(element1 / element2)
    if operator == '%':
        return element1 % element2


def rpn_evaluation(rpn_exp):
    results_list = []
    operator_list = ['+', '-', '*', '/', '%']

    try:
        for element in rpn_exp.split():
            if element in operator_list:
                operator2 = results_list.pop()
                operator1 = results_list.pop()
                results_list.append(do_operation(operator1, operator2, element))
            elif element.isnumeric():
                results_list.append(int(element))
            elif re.search(floating_point_regex, element):
                raise Exception('Floating-point numbers are not accepted.')
            else:
                raise Exception('Invalid character')
    except IndexError:
        print('Invalid RPN expression')

    return results_list.pop() if len(results_list) > 0 else 0


if __name__ == '__main__':
    print('Type the RPN expression that you want to evaluate:')
    rpn_exp = input()

    print('The result of the RPN expression is:', rpn_evaluation(rpn_exp))
