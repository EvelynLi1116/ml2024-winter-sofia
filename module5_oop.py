class Integer_Checker():
    def __init__(self):
        pass

    def initialization(self):
        N = int(input('Please provide a positive integer number:'))
        return N

    def insertion(self):
        N = self.initialization()
        l_ = []
        for i in range(N):
            l_.append(int(input('Please provide an integer number:')))
        return l_

    def search(self):
        l_ = self.insertion()
        checker = int(input('Please provide another integer number:'))
        if checker in l_:
            return l_.index(checker)+1
        else:
            return -1

