##############################################################################
#   OS11 LOGISTICS
#
#   Author   : Orge, Fernando Gabriel
#   Exercise : EX08 - Transshipment Problem
#   
#   Solution for Product A1 or simply A
#
#   SOLVING PROBLEM WITH SIMPLEX
#	   The raw solution will be: [20.  0. 10.  0. 30.  0. 30. 10. 20.  0.  0.  0.]
#	       20 units will be moved across P1 --> W1 arc
#	        0 units will be moved across P1 --> W2 arc
#	       10 units will be moved across P2 --> W1 arc
#	        0 units will be moved across P2 --> W2 arc
#	       30 units will be moved across P3 --> W1 arc
#	        0 units will be moved across P3 --> W2 arc
#	       30 units will be moved across W1 --> S1 arc
#	       10 units will be moved across W1 --> S2 arc
#	       20 units will be moved across W1 --> S3 arc
#	        0 units will be moved across W2 --> S1 arc
#	        0 units will be moved across W2 --> S2 arc
#	        0 units will be moved across W2 --> S3 arc
#	   The minimum cost will be: 18000.00
#
#      Move all units from every plant to warehouse 1.
#      Then move all units from Warehouse 1 to every salepoint.
#
#
##############################################################################
import numpy     as np
import logistics as lg
from   scipy.optimize import  linprog

nodes = ['P1','P2','P3','W1','W2','S1','S2','S3']
NN_PW = np.array([[0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])
               
NN_WS = np.array([[0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

A_ub, arcs_ub = lg.nn2na(NN_PW, nodes)      # node-arc matrix and list of arcs
A_eq, arcs_eq = lg.nn2na(NN_WS, nodes)      # node-arc matrix and list of arcs
for i in range(0, len(nodes)):
    for j in range(0, len(arcs_ub)):
        if i <= 2:
            A_eq[i,j] = 0
        if i >= 3:
            A_ub[i,j] = 0
b_ub = np.array([ 20,  10,  30,   0,   0,   0,   0,   0])
b_eq = np.array([  0,   0,   0,   0,   0, -30, -10, -20])
c = np.array([100, 100, 150, 150, 200, 200, 100, 150, 200, 100, 150, 200])
bounds = tuple([(0, None) for arcs in range(0, len(arcs_ub))])

print('\t OPTIMIZER INPUTS                                   \n'
      '\t     Cost vector                             :   %s \n'
      '\t     A_ub Node-Arc from Plants to Warehouses : \n%s \n'
      '\t     b_ub supply vector                      :   %s \n'
      '\t     A_eq Node-Arc from Warehouses to Sales  : \n%s \n'
      '\t     b_ub demand vector                      :   %s \n'
      '\t     Bounds of each X arc variable           :   %s \n' % (c, A_ub, b_ub, A_eq, b_eq, bounds))

print('\n SOLVING PROBLEM WITH SIMPLEX')
res = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds, method='simplex')
print('\t Solution to the problem:')
print('\t   The raw solution will be: %s' % res.x)
for k in range(0, len(arcs_ub)):
    print('\t       %2d units will be moved across %s arc' % (res.x[k], arcs_ub[k]))
print('\t   The minimum cost will be: %0.2f ' % res.fun)
