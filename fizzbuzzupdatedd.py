###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################

def fizzbuzz(n):
    # Declare a list of strings to store the results
    result = []

    # Loop ffrom 1 to n (inclusive)
    for i in range(1, n+1):

        # Check if i is divisible by both 3 and 5
        if i%3 == 0 and i%5 == 0:

            #Add "Fizzbuzz" to the result list 
            result.append("Fizzbuzz")

        # Check if i is divisible by 3
    elif i%3 == 0: 

        #Add "Fizz" to the result list 
        result.append("Fizz")

    # Check if i is divisible by  5
elif i % 5 == 0: 

        # Add "Buzz" to the result list
        result.append("Buzz")

    else: 
        # Add the current numbber as a string to the 
        # result list 
        result.append(str(i))

    #  Return the result list 
    return result 



    