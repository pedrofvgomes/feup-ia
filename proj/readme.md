# Inteligência Artifical - Projeto

## Topic 3: Metaheuristics for Optimization/Decision Problems
- An optimization problem is characterized by the existence of a (typically large) set of possible solutions, comparable to each other, of which one or more are considered (globally) optimal solutions.
- Depending on the specific problem, an evaluation function allows you to establish this comparison between solutions. In many of these problems, it is virtually impossible to find the optimal solution or to ensure that the solution found is optimal, and, as such, the goal is to try to find  locally optimal solution that maximizes/minimizes a given evaluation function to the extent possible.
- In this work, the aim is to implement a system to solve an optimization problem, using different algorithms or meta-heuristics, such as hill-climbing, simulated annealing, tabu search, and genetic algorithms (you may include other algorithms or variations of these). 
- Multiple instances of the chosen problem must be solved, and the results obtained by each algorithm must be compared. Different parameterizations of the algorithms should be tested and compared, in terms of the average quality of the solution obtained and the average time spent to obtain the solutions. All problems should have different sizes/difficulties to solve. The application to be developed should have an appropriate visualization in text or graphic mode, to show the evolution of the quality of the solution obtained along the way and the final (i.e. local optimal) solution, and to interact with the user.
- You should allow the selection and parameterization of the algorithms and the selection of the instance of the problem to be solved.

## Chosen theme - Book Scanning (instructions [here](./instructions.pdf))


### Problem description
```
BOOKS
- there are B different books
- many libraries can have a copy of the same book, but we only need
to scan each book once
- each book is described by one parameter: the score that's awarded 
when it's scanned

LIBRARIES
- there are L different libraries
- each library is described by the following parameters:
    - the set of books in the library
    - the time in days that it takes to sign the library up for scanning
    - the number of books that can be scanned each day once 
    it's signed up

TIME 
- there are D days, from 0 to D-1
- the first library can be start on day 0, D-1 is the last day
during which days cabn be shipped to the scanning facility

LIBRARY SIGNUP
- each library has to go through the signup process before books 
from there can be shipped
- the signup process for a library can start only when there are no 
other signup processes running
- they can be signed up in any order
```

### Input data set
```
Plain-text files, delimited by '\n' characters.
For state-management purposes, we'll name these stages from A to C

- First line: B L D
- Second line: S[0], S[1], ..., S[B-1]

L sections, each describing individual libraries
- First line: N T M
- Second line: ID[0], ID[1], ..., ID[N-1]
```