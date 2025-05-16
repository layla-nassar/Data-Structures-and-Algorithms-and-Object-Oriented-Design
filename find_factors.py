def find_factors(numbers):
    # Initialize an empty dictionary to hold the numbers and their factors
    factors_dict = {}
    
    # Iterate through each number in the input list
    for num in numbers:
        # Find factors of num by checking for even division with all numbers in the list
        factors = [factor for factor in numbers if num % factor == 0]
        # Add the number and its factors to the dictionary
        factors_dict[num] = factors
        
    return factors_dict

# Example input
input_list = [6, 7, 18, 1, 3]

# Call the function with the example input
result = find_factors(input_list)
print(result)