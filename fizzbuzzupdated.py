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

def fizzbuzz(start, finish):
    '''This function prints numbers from start to finish replacing multiples of 3 with fizz, multuples of 5 with buzz, and multiples of both with fizzbuzz'''
    for i in range(start, finish+1):
        if i%3 == 0 and i%5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print('buzz')
        else: 
            print(i)

    