import copy

class Matrix(object):
    
    def __init__(self,X):
        if not isinstance(X,list):
            raise TypeError('Matrices require a list of lists')

        if not isinstance(X[0],list):
            raise TypeError('Matrices require a list of lists')

        columns = len(X[0])
        
        for i in X:
            if len(i) != columns:
                raise TypeError('The matrix is not well-formed')

        self.list = X

    def __getitem__(self,index):
        return self.list[index[0]][index[1]]

    def __setitem__(self,index,value):
        self.list[index[0]][index[1]] = value

    def rows(self):
        return len(self.list)

    def cols(self):
        return len(self.list[0])

    def __str__(self):
        string_rep = "";
        for i in range(self.rows()):
            string_rep += "[ "
            for j in range(self.cols()):
                string_rep += str(self[i,j]) + ' '
            string_rep += "]\n"               

        return string_rep    

    def __add__(self,X):
        if self.rows() != X.rows():
            raise TypeError('Dimension (row) mismatch')
        if self.cols() != X.cols():
            raise TypeError('Dimension (column) mismatch')

        result = copy.deepcopy(self)

        for i in range(self.rows()):
            for j in range(self.cols()):
                result[i,j] = result[i,j] + X[i,j]

        return result
    
    def __sub__(self,X):
        if self.rows() != X.rows():
            raise TypeError('Dimension (row) mismatch')
        if self.cols() != X.cols():
            raise TypeError('Dimension (column) mismatch')

        result = copy.deepcopy(self)

        for i in range(self.rows()):
            for j in range(self.cols()):
                result[i,j] = result[i,j] - X[i,j]

        return result

    def gq(self,t,l):
        result = Matrix([[0] * (self.rows()//2) \
                         for i in range(self.rows()//2)])
        t *= self.rows() // 2
        l *= self.cols() // 2

        for i in range(result.rows()):
            for j in range(result.cols()):
                result[i,j] = self[t+i,l+j]

        return result

    def sq(self,t,l,X):
        t *= self.rows() // 2
        l *= self.cols() // 2

        for i in range(X.rows()):
            for j in range(X.cols()):
                self[t+i,l+j] = X[i,j]
    
    def strassen(self,Bs,Cs):
        M1 = (self.gq(0,0) + self.gq(1,1))*(Bs.gq(0,0) + Bs.gq(1,1))
        M2 = (self.gq(1,0) + self.gq(1,1))*Bs.gq(0,0)
        M3 = self.gq(0,0)*(Bs.gq(0,1) - Bs.gq(1,1))
        M4 = self.gq(1,1)*(Bs.gq(1,0) - Bs.gq(0,0))
        M5 = (self.gq(0,0) + self.gq(0,1))*Bs.gq(1,1)
        M6 = (self.gq(1,0) - self.gq(0,0))*(Bs.gq(0,0)+Bs.gq(0,1))
        M7 = (self.gq(0,1) - self.gq(1,1))*(Bs.gq(1,0) + Bs.gq(1,1))

        Cs.sq(0,0,M1 + M4 - M5 + M7)
        Cs.sq(0,1,M3 + M5)
        Cs.sq(1,0,M2 + M4)
        Cs.sq(1,1,M1 + M3 - M2 + M6)

        return Cs

    def naive_mul(self,X):
        result = Matrix([[0] * X.cols() \
                         for i in range(self.rows())])

        for i in range(self.rows()):
            for j in range(X.cols()):
                sum = 0
                for k in range(self.cols()):
                    sum += self[i,k] * X[k,j]
                result[i,j] = sum
        return result

    def __mul__(self,X):
         # Scalar multiplication
        if not isinstance(X,Matrix):
            result = copy.deepcopy(self)
            
            for i in range(self.rows()):
                for j in range(self.cols()):
                    result[i,j] = self[i,j] * X
            return result
        
        if self.cols() != X.rows():
            raise TypeError('Dimension mismatch')

        result = Matrix([[0] * X.rows() \
                         for i in range(self.rows())])

        # For the case of a 1 x 1 matrix
        if self.rows() <= 1 and self.cols() <= 1:
            if X.rows() <= 1 and X.cols() <= 1:
                result[0,0] = self[0,0] * X[0,0]
                result = self.naive_mul(X)
                return result

        return self.strassen(X,result)


                    

    
