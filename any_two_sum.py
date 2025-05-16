def  any_two_sum(numbers, total): 
    'checks to see if only 2 numbers in a set are equal to a certain sum  '
    num_set = set()
    for i in numbers:
        if total - i in num_set:
            return True
        else:
            num_set.add(i)
    return False