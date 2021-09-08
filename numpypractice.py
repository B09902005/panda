import numpy

one1 = numpy.array([3,5,1,2,9])
one2 = numpy.zeros(5)
one3 = numpy.ones(5)
one4 = numpy.arange(5)
'''
print(one1)
print(one2)
print(one3)
print(one4,'\n')
'''

two0 = numpy.array([[1,5,7],[3,6,8]])
two1 = numpy.array([[3,5,1],[2,9,0]])
two2 = numpy.zeros([2,3])
two3 = numpy.ones([2,3])
two4 = numpy.array([[2,4],[7,1],[3,6]])
'''
print(two1)
print(two2)
print(two3)
print(two3.size,'\n')

print(two4[0])
print(two4[0][1])
print(two4[0:2])
print(two4[0:2][:1])
print(two4[0:2,:1])
print(two4[...,1])

print(two1.sum())
print(two1.sum(axis = 0)) # add column
print(two1.sum(axis = 1)) # add row
print(two1.cumsum()) # cumulative sum
print(two1.mean())
print(two1.mean(axis = 0),'\n')

print(two0 + two1)
print(two0 * two1)
print(two0 <= two1)
print(two0 @ two4)  # matrix multiply
print(numpy.outer(two0, two4),'\n') # outer product

print(one1.shape)
print(two0.shape)
print(two4.shape)
print(two4.T)
print(two4.ravel())
print(two4.reshape(2,1,3))  # expand to 1D
print(numpy.arange(16).reshape(4,4).T)
'''
