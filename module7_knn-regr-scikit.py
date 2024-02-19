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
        x_ = np.array([])
        y_ = np.array([])
        for i in range(N):
            x = np.float(input('Please provide a real number x:'))
            if x_.size == 0:
                x_ = np.append (x_, [x])
            else:
                x_ = np.vstack([x_,[x]])
                
            y = np.float(input('Please provide a real number y:'))
            if y_.size == 0:
                y_ = np.append (y_, [y])
            else:
                y_ = np.vstack([y_,[y]])
                
        return N, x_, y_

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
