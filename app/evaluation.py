import argparse

parser = argparse.ArgumentParser(description="RPN expression calculator - options")
parser.add_argument('--expr', help='Type the RPN expression for evaluation inside quotes', required=False)

args = parser.parse_args()


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

    for element in rpn_exp.split():
        if element in operator_list:
            operator2 = results_list.pop()
            operator1 = results_list.pop()
            results_list.append(do_operation(operator1, operator2, element))
        elif element.isnumeric():
            results_list.append(int(element))
        else:
            raise Exception('Invalid character')

    return results_list.pop() if len(results_list) > 0 else 0


if __name__ == '__main__':
    print('The result of the RPN expression is:', rpn_evaluation(args.expr))
