
def contains_permutation(input_string, pattern): 
    'checks a string for a specfic amount of characters'
    pattern_a = set(pattern)
    count = 0
    pattern_list = []
    for char in input_string:
        if char in pattern_a: 
            count += 1 
            pattern_list.append(char)
    check = ''.join(pattern_list)
    if check == pattern: 
        return True 
    if count == len(pattern):
        return True
    else:
        return False 
    
'''
def contains_permutation(input_string, pattern):
    'checks a string for a certain pattern of characters'
    open_set = {}
    str_set ={}
    count = len(pattern)
    str_check = input_string.lower()

    for i in pattern:
        open_set[i] = open_set.get(i,0)+1
    for h in range(count):
        str_set[str_check[h]] = str_set.get(h,0)+1

    count_cont = len(input_string)

    for j in range(count, count_cont):
        if open_set == str_set:
            return True
        str_set[str_check[j-count]] -=1
        if str_set[str_check[j-count]] == 0:
            del str_set[str_check[j - count]]
        str_set[str_check[j]] = str_set.get(str_check[i], 0)+1
        if str_set == open_set:
            return True



    return False
    '''