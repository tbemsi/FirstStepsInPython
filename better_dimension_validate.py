__author__ = 'bemsibom'

## python varargs keyword arguments


def dim_validate(*args, **kwargs):
    result = True
    for arg in args:
        result = result and (
            isinstance(arg, Number) and arg >=0
        )
    for key in kwargs:
        result = result and (
            isinstance(kwargs[key], Number) and kwargs[key] >=0
        )
    return result

def test_one_correct_arg():
    assert dim_validate(1) == True