## ex07-08-dynamic-networks-and-transshipment-fernandoorge

### Table of contents
* [Repo organization](#repo-organization)
* [Solution to exercise 07](#solution-to-exercise-07)
* [Solution to exercise 08](#solution-to-exercise-08)
  * [Solution for product A1](#solution-for-product-a1)
  * [Solution for product A2](#solution-for-product-a2)
  * [Solution for both products](#solution-for-both-products)

### Repo organization

Each exercise of the assignment is solved in a different file
* ex07.py for exercise 07
* ex08.py for exercise 08

*basic_utils.py* contains some useful functions developed by the professor.

*logistics.py*  constains some useful functions developed by me. The required 
algorithms to complete the assignment can be found there.


### Solution to exercise 07

Work in progress...

### Solution to exercise 08

#### Solution for product A1

```
    SOLVING PROBLEM WITH SIMPLEX
    The raw solution will be: [20.  0. 10.  0. 30.  0. 30. 10. 20.  0.  0.  0.]
       20 units will be moved across P1 --> W1 arc
        0 units will be moved across P1 --> W2 arc
       10 units will be moved across P2 --> W1 arc
        0 units will be moved across P2 --> W2 arc
       30 units will be moved across P3 --> W1 arc
        0 units will be moved across P3 --> W2 arc
       30 units will be moved across W1 --> S1 arc
       10 units will be moved across W1 --> S2 arc
       20 units will be moved across W1 --> S3 arc
        0 units will be moved across W2 --> S1 arc
        0 units will be moved across W2 --> S2 arc
        0 units will be moved across W2 --> S3 arc
    The minimum cost will be: 18000.00
```

*Conclusions*

* Move all units from every plant to warehouse 1.
* Then move all units from Warehouse 1 to every salepoint.
* Since the costs of moving a unit from every plant to any warehouse are equal (i.e. cost(P1, W1) = cost(P1, W2), the algorithm ignores the second warehouse (W2) and gives us a solution where all units are moved to the first warehouse (W1).
* Considering that there's no limitation in warehouse's capacity, this solution is feasible
      
#### Solution for product A2

```
    SOLVING PROBLEM WITH SIMPLEX
    Solution to the problem:
    The raw solution will be: [30.  0. 40.  0. 10.  0. 40. 20. 20.  0.  0.  0.]
       30 units will be moved across P1 --> W1 arc
        0 units will be moved across P1 --> W2 arc
       40 units will be moved across P2 --> W1 arc
        0 units will be moved across P2 --> W2 arc
       10 units will be moved across P3 --> W1 arc
        0 units will be moved across P3 --> W2 arc
       40 units will be moved across W1 --> S1 arc
       20 units will be moved across W1 --> S2 arc
       20 units will be moved across W1 --> S3 arc
        0 units will be moved across W2 --> S1 arc
        0 units will be moved across W2 --> S2 arc
        0 units will be moved across W2 --> S3 arc
    The minimum cost will be: 26000.00
```

*Conclusions*

* Move all units from every plant to warehouse 1.
* Then move all units from Warehouse 1 to every salepoint.
* Since the costs of moving a unit from every plant to any warehouse are equal (i.e. cost(P1, W1) = cost(P1, W2), the algorithm ignores the second warehouse (W2) and gives us a solution where all units are moved to the first warehouse (W1).
* Considering that there's no limitation in warehouse's capacity, this solution is feasible


#### Solution for both products

**The solution for both products can be thought as the linear combination of solution A and solution B, due to the following reasons**:

* The graph of product A1 (or simply A) is completely independant of the graph of product A2 (or B).
* There is no stock limit in the warehouses. The products doest not compite with each other.
