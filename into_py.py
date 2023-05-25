from functools import reduce

def into(result_variable, iterable, function):
    result_variable = reduce(function, iterable)
    return result_variable
