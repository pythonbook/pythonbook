class Vector(tuple):
  def __init__(self,x):
    tuple.__init__(x)

  def __add__(self,X):
    if len(self) != len(X):
      raise TypeError ('Dimension mismatch')
    result = []
    for i in range(len(self)):
      result.append(self[i]+X[i])
    return Vector(result)

  def __iadd__(self,X):
    return self.__add__(X)

  def __sub__(self,X):
    if len(self) != len(X):
      raise TypeError ('Dimension mismatch')
    result = []
    for i in range(len(self)):
      result.append(self[i]-X[i])
    return Vector(result)

  def __isub__(self,X):
    return self.__sub__(X)

  def __mul__(self,X):
    if len(self) != len(X):
      raise TypeError ('Dimension mismatch')
    result = 0
    for i in range(len(self)):
      result += self[i]*X[i]
    return result

  def __imul__(self,X):
    return self.__mul__(X)

  def __xor__(self,X):
    if len(self) != len(X):
      raise TypeError('Dimension mismatch')
    if len(self) < 2:
      return Vector([0]*len(self))
    elif len(self) > 3:
      raise NotImplementedError
    elif len(self) == 2:
      return Vector(0,0,self[0]*X[1] - X[0]*self[1])
    else:
      return Vector((self[1]*X[2] - X[1]*self[2],
              self[2]*X[0] - X[2]*self[0],
              self[0]*X[1] - X[0]*self[1]))

  def __ixor__(self,X):
    return self.__xor__(X)
