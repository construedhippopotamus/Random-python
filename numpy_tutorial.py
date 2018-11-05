# -*- coding: utf-8 -*-
"""
Numpy tutorial

http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html

additional practice, didn't do these:
  http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html  

"""
import numpy as np

#create array with specified range
A = np.arange(1,10,1)
#print( A )

#10x10x10 of randoms
#print (np.random.random((10,10,10)) )

#zero array
B = np.zeros([8,8],dtype=int)


#CHECKERBOARD   :: means skip row
#[rstart=r1:rend=end:rstep=2, cstart=c0:cend=end:cstep=2]
B[1::2,::2] = 1
B[::2, 1::2] = 1

#print( B  )


#10x10 of random values, find min/max
C = np.random.random((10,10))
#print( C, "\n \n max: ", np.max(W),"\n \n min: ", np.min(W) )

#3. checkerboard 8x8 with tile function
# first row is repeat 0,1 four times; 2nd is repeat 1,0
#(4,4) is repeat(row, col), which is how the 8x8 generates
D = np.tile( np.array([[0,1],[1,0]]), (4,4)  )
#print( D )

#4. normalize a 5x5 random matrix btwn 0-1

#random matrix:
E = np.random.random((5,5))
Emax, Emin = E.max(), E.min()
E = (E - Emin)/(Emax-Emin)

#print( E )

#5. multiply 5x3 matrix by 3x2 matrix (real matrix product)
F = np.random.random((5,3))
G = np.random.random((3,2))
H = np.matmul(F, G)
# np.dot(F, G)  # this also works
#print( H )

#6. 10x10 matrix with row values from 0-9
I = np.zeros((10,10))
I += np.arange(10)
#print( I )

#8. sort a random vector of size 100
J = np.random.random((100))
J = np.sort(J)
#print( J )

#9. check if random matrix A == B
#print( np.random.random((10,10)) ==np.random.random((10,10)) )

#Apprentice problems
#------------------------------------

#2. replace max by zero
K = np.random.random((100))
#print("initial max", K.max())
K[np.argmax(K)] = 0
#print("new max", K.max())

#3. Declare a structured array with x and y coordinates covering the [0,1]x[0,1] area.
# structured array: like a dictionary: x = np.array([('age', 10), ('height', 5, 6 ] )
# x['age'] --> 10

#create structured array:
L = np.zeros((10,10), [('x',float),('y',float)])
# np.linspace(start, stop, interval) --> creates even distribution btwn start, stop
L['x'], L['y'] = np.meshgrid(np.linspace(0,1,10),
                             np.linspace(0,1,1))
#print(L)