def convert_to_container(element, nested=False):
    if element is None:
        return element
    elif is_container(element):
        return (element,) if nested else element
    else:
        return (element,)


def is_container(element):
    return not isinstance(element, str) and hasattr(element, "__iter__")


def is_dict_subset(smaller, larger):
    """
    Given: dicts, smaller and larger
    Return: are the keys and values in smaller a subset of larger
    """
    return all(
        larger.get(smaller_key, None) == smaller_val
        for smaller_key, smaller_val in smaller.items()
    )


def is_subarray(a, b):
    """
    Given: sequences a and b
    Return: boolean, a is a subarray of b
    """
    a_pointer, b_pointer = 0, 0
    len_a, len_b = len(a), len(b)
    while a_pointer < len_a and b_pointer < len_b:
        if a[a_pointer] == b[b_pointer]:
            a_pointer += 1
            b_pointer += 1
            if a_pointer == len_a:
                return True
        else:
            a_pointer = 0
            b_pointer += 1
    return False


def nested_dict_get(d, keys):
    result = d
    for key in keys:
        try:
            result = result.get(key, dict())
        except AttributeError:
            result = dict()
    return result


def nested_dict_set(d, keys, value):
    nested_dict_get(d, keys[:-1])[keys[-1]] = value
