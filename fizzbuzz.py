def fizzbuzz(start, finish):
    '''This function returns fizz when there is a multiple of three and buzz when there is a multiple off 5 and fizzbuzz if both'''
    for num in range(start, finish + 1):
        output = str()

        # Check for multiples of 3
        if (num % 3 == 0) or ("3" in str(num)):
            output += "fizz"

        # Check for multiples of 5
        if (num % 5 == 0) or ("5" in str(num)):
            output += "buzz"

        # If no conditions are met, print the number
        if output != "" :
            print(output)

        else:
            print(num)