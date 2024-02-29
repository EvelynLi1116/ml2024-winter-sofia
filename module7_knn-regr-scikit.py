import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

class KNN_Regressor():
    def __init__(self):
        pass

    def initialization(self):
        N = np.int(input('Please provide a positive integer number N:'))
        return N
    
    def neighbors(self):
        k = np.int(input('Please provide a positive integer number k:'))
        return k

    def insertion(self):
        N = self.initialization()
        x_ = []
        y_ = []
        for i in range(N):
            x = np.float(input('Please provide a real number x:'))
            x_.append(x)
                
            y = np.float(input('Please provide a real number y:'))
            y_.append(y)
                
        return N, np.array(x_), np.array(y_)

    def knn(self):
        N, x_, y_ = self.insertion()
        k = self.neighbors()
        
        if k <= N:
            neigh = KNeighborsRegressor(n_neighbors=k)
            neigh.fit(x_,y_)
            Y = neigh.predict(x_)
            r_square = r2_score(y_, Y)
            
            return Y, r_square
        
        else:
            raise ValueError('inputted nearest neighbors "k" is greater than total neighbors "N"')
