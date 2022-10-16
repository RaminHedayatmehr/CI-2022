Explanation of the algorithm.

The main idea of the algorithm is to cover the universe taking every time the apparently most convenient set in the sets list. In other words: every while cycle the program will search among all sets and will take the one with the highest ratio between the elements not yet covered and the relative cost of the set. This algorithm doesn’t always give the best result, but certainly it gives an optimal one.
The solution is not exactly what was asked for,but it tries to compare GREEDY algorithm in compare to BRANCH and BOUND algorithm.
Also the whole process is done on a set without weight.
