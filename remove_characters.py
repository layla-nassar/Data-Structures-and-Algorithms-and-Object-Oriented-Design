def remove_characters(input_string, to_remove):
    'returns a string with certain characters removed'
    n_str = set(to_remove)
    ne_str = []
    for char in input_string:
        if char not in n_str: 
            ne_str.append(char)

    return ''.join(ne_str)
