algebraic_expression = input()
parentheses = []

for i in range(len(algebraic_expression)):
    if algebraic_expression[i] == "(":
        parentheses.append(i)

    elif algebraic_expression[i] == ")":
        start_index = parentheses.pop()
        end_index = i + 1
        print(algebraic_expression[start_index:end_index])
