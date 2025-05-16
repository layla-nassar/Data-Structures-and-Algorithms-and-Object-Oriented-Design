import time

def time_function(func, args, n_trials=10):
    """This function will return the number of seconds with arg."""
    start_time = time.time()
    func(args)
    end_time = time.time() - start_time
    min_time = float('inf')
    for i in range(n_trials):
        min_time
    return end_time 

def unpack(func, args):
    return func(*args)
    
def time_function_flexible(func, args_tuple, n_trials=10):
    """This function when it's called will unpack the tuple of arguments."""
    lis = []
    for i in range(n_trials):
        start_time = time.time()
        unpack(func, args_tuple)
        final_time = time.time()
        lis.append(final_time - start_time)
    return min(lis)
    


if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function(test_func, L2)

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))