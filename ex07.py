##############################################################################
#   OS11 LOGISTICS
#
#   Author   : Orge, Fernando Gabriel
#   Exercise : EX07 - Dynamic Network Flows - Emergency Evacuation Plan
#
#       Hence, the Node-Node Matrix will be
#             s a b t 
#           s 0 1 1 0
#           a 0 0 1 1
#           b 0 0 0 1
#           t 0 0 0 0
#
##############################################################################
import numpy     as np
import logistics as lg
from   scipy.optimize import  linprog

#              s0 s1 s2 s3 s4 s5 s6 a1 a2 a3 a4 a5 a6 b1 b2 b3 b4 b5 b6 t1 t2 t3 t4 t5 t6 t0
G = np.array([[ 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #s0
              [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #s1
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], #s2
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], #s3
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #s4
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #s5
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #s6
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #a1
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], #a2
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], #a3
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], #a4
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], #a5
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #a6
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #b1
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], #b2
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], #b3
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], #b4
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], #b5
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #b6
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #t1
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #t2
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #t3
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #t4
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #t5
              [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #t6
              [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])#t0

NA, arcs = lg.nn2na(G)
(num_nodes, num_arcs) = NA.shape

##  beq vector
##      All zeros - Dimension nodes
b = np.zeros(num_nodes)

##  Costs vector
##      All zeros except for the last element
c = np.zeros(num_arcs)
c[-1] = -1

##  Lower bounds (capacity)
##      No restrictions here
l = np.zeros(num_arcs)

##  Upper bounds (capacity)
##      We have a capacity restriction for each possible arc
u = np.array([None,  # (s0, s1)
              None,  # (s0, s2)
              None,  # (s0, s3)
              None,  # (s0, s4)
              None,  # (s0, s5)
              None,  # (s0, s6)
                 5,  # (s1, a2)
                10,  # (s1, b4)
                 5,  # (s2, a3)
                10,  # (s2, b5)
                 5,  # (s3, a4)
                10,  # (s3, b6)
                 5,  # (s4, a5)
                 5,  # (s5, a6)
                 6,  # (a1, b3)
                 3,  # (a1, t2)
                 6,  # (a2, b4)
                 3,  # (a2, t3)
                 6,  # (a3, b5)
                 3,  # (a3, t4)
                 6,  # (a4, b6)
                 3,  # (a4, t5)
                 3,  # (a5, t6)
                 3,  # (b1, t2)
                 3,  # (b2, t3)
                 3,  # (b3, t4)
                 3,  # (b4, t5)
                 3,  # (b5, t6)
              None,  # (t1, t0)
              None,  # (t2, t0)
              None,  # (t3, t0)
              None,  # (t4, t0)
              None,  # (t5, t0)
              None,  # (t6, t0)
              None]) # (t0, s0)

if len(u) != len(l):
    print('ERROR: u vector is not properly set')

##############################################################################
# Inputs lo linprog algorithm
C   = c
Aeq = NA
beq = b
bounds = []
for k in range(0, len(l)):
    bound_tuple = (l[k], u[k])
    bounds.append(bound_tuple)

print('\t OPTIMIZER INPUTS                         \n'
      '\t     Cost vector                   :   %s \n'
      '\t     A_eq Node-Arc matrix          : \n%s \n'
      '\t     b_eq demand-supply vector     :   %s \n'
      '\t     Bounds of each X arc variable :   %s \n' % (C, Aeq, beq, bounds))

name_method = 'simplex'
print('\n*****************************************************************')
print('\t SOLVING PROBLEM WITH: %s' % name_method)
res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method=name_method)
print('\t Solution to the problem:')
print('\t   The raw solution will be: %s' % res.x)
#for k in range(0, len(res.x)):
#    if res.x[k] > 0:
#        print('\t\t %d units must be moved across %s arc.' 
#            % (res.x[k], str(lg.convert_arc(arcs[k], nodes))))
print('\t   The maximum flow will be: %0.2f ' % abs(res.fun))
print('*****************************************************************\n')
