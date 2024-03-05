import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

class KNNClassifier():
    def __init__(self):
        pass

    def initialization(self):
        N = np.int(input('Please provide a positive integer number:'))
        return N

    def insertion(self):
        N = self.initialization()
        x_ = []
        y_ = []
        for i in range(N):
            x = np.float(input('Please provide a real number x:'))
            x_.append([x])
                
            y = np.float(input('Please provide a non-negative integer y:'))
            y_.append([y])
                 
            
        return np.array(x_), np.array(y_)

    def best_model(self):
        x_train, y_train = self.insertion()
        x_test, y_test = self.insertion()
        
        params = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
        
        gs_knn = GridSearchCV(KNeighborsClassifier(),
                              param_grid=params,
                              scoring='accuracy',
                             cv=2)
        
        gs_knn.fit(x_train, y_train)
        
        params = gs_knn.best_params_
        accuracy = gs_knn.score(x_test, y_test)
        
        return params, accuracy
