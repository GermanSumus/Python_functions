# Test user input for Conformation/Continuation
def test():
    try:
        test = input('Are you sure? ("N" or Enter to continue)\n> ')
        print(test)
        if test.upper() == 'Y' or test == '':
            return True
        elif test.upper() == 'N':
            return False
    except:
        return False

