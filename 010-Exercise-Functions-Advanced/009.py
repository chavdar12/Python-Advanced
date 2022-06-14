def func_executor(*args: tuple):
    functions_results = []
    for func, nums in args:
        result = func(*nums)
        functions_results.append(result)

    return functions_results
