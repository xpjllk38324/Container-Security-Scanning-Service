**Task 8 Report**
**Classical Software Design Solutions**

This repository contains solutions for two classical software design problems using Python: the Key Word in Context (KWIC) problem and the Eight Queens (8Q) problem. The objective was to apply different software design methods to each problem and analyze their effectiveness

Problem Descriptions

**Problem A: Key Word in Context (KWIC)**
KWIC involves displaying phrases or lines with a specific word centered within its context. In this implementation, the Abstract Data Types (ADT) approach was used, where classes represent core concepts of the problem (e.g., KWICSystem and LineStorage).

**How to Run**

Ensure Python 3 is installed.
To execute, run:

python kwic_solution.py

**Sample Input:**

Phrases: "Design patterns are useful for problem-solving"

"Programming paradigms vary across languages"


**Sample Output:**

Design patterns are useful for problem-solving

patterns are useful for problem-solving Design


**Problem B: Eight Queens (8Q)**


The Eight Queens problem entails placing eight queens on a chessboard such that no two queens threaten each other. Here, the Pipes-and-Filters design method was used, breaking down the solution into separate functions operating on the data in sequence.

**2. Eight Queens Solution (Using Pipes-and-Filters)**
   
This solution treats each function as an independent "filter," processing the board data sequentially. Each function checks constraints or places queens independently, passing the data down the pipeline.

Functions Used:
generate_empty_board: Initializes an empty chessboard.
is_safe: Validates safe queen placements.
place_queens: Recursively places queens on the board and stores valid solutions.

**How to Run**

Ensure Python 3 is installed.
To execute, run:

python eight_queens_solution.py

Output:

Each solution is printed as a board layout, with Q indicating queen positions.

## Solution Comparison Table

| Feature                   | KWIC (ADT)   | Eight Queens (Pipes-and-Filters) |
|---------------------------|--------------|----------------------------------|
| Algorithm Flexibility     | High         | Medium                           |
| Data Representation Change| Moderate     | High                             |
| Additional Functions      | Easy         | Moderate                         |
| Performance               | Moderate     | High                             |
| Reusability               | Moderate     | High                             |


Algorithm Flexibility: The ADT method offers more flexibility in modifying the KWIC algorithm.

Data Representation: Pipes-and-Filters is highly adaptable, making data representation changes relatively simple.

Additional Functions: It is easier to add functions within the ADT approach due to encapsulation.

Performance: Pipes-and-Filters tends to be more performant due to its linear processing flow.

Reusability: The modularity of Pipes-and-Filters increases reusability for future projects.

