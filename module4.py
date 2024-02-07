def integer_checker():
    N = int(input('Please provide a positive integer number:'))
    
    l_ = []
    for i in range(N):
        l_.append(int(input('Please provide an integer number:')))
        
    checker = int(input('Please provide another integer number:'))
    if checker in l_:
        return l_.index(checker)+1
    else:
        return -1

    
test_call = integer_checker()
