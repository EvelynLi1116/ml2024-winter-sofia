import numpy as np
from sklearn.metrics import precision_score, recall_score

class Metrics():
    def __init__(self):
        pass

    def initialization(self):
        N = np.int(input('Please provide a positive integer number N:'))
        return N

    def insertion(self):
        N = self.initialization()
        x_ = []
        y_ = []
        for i in range(N):
            x = np.float(input('Please provide a boolean number x (0 or 1):'))
            x_.append(x)
                
            y = np.float(input('Please provide a boolean number y (0 or 1):'))
            y_.append(y)
                 
        return np.array(x_), np.array(y_)

    def precision_recall(self):
        x_, y_ = self.insertion()
        
        precision=precision_score(x_, y_)
        
        recall=recall_score(x_, y_)
        
        return precision, recall
