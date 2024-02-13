import numpy as np

class Integer_Checker():
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
        arr = np.array([])
        for i in range(N):
            x = np.int(input('Please provide a real number x:'))
            y = np.int(input('Please provide a real number y:'))
            if arr.size > 0: 
                arr = np.vstack([arr,[x,y]])
            else:
                arr = np.append (arr,[x,y])
        return N, arr

    def knn(self):
        N, arr = self.insertion()
        k = self.neighbors()
        X = np.int(input('Please provide another real number X:'))
        
        if k <= N:
            dist = np.array([])
            for pair in arr:
                x_d = np.abs(pair[0]-X)
                y = pair[1]
                if dist.size > 0:
                    dist = np.vstack([dist,[x_d,y]])
                else:    
                    dist = np.append(dist,[x_d,y])
                    
            dist = dist[np.argsort(dist[:, 0])]
            Y = 0
            for i in range(k):
                Y += dist[i][1]
                
            return Y/k
        
        else:
            raise ValueError('inputted nearest neighbors "k" is greater than total neighbors "N"')
