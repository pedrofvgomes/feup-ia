# Book Scanning Application

## Overview

This application optimizes the book scanning process for libraries, employing algorithms to maximize the score of scanned books within a given time frame. The score is awarded once for each book scanned, regardless of the number of library copies.

## System Requirements

- Python 3.7 or higher

## Installation

To run the application, install PyQt5 via pip:

```bash
pip install PyQt5
```

## Running the Application

Execute the following in the command line at the `proj` folder:

```bash
python main.py
```

## Usage Instructions

1. **Import Libraries**: Use 'Import Libraries' to load the data file.
2. **Select Algorithm**: Choose an algorithm for processing.
3. **Apply Algorithm**: The chosen algorithm processes the data, and the total score is displayed.
4. **Results**: A submission file is created in `proj/output`.

## Problem Description

**Books:**
- B unique books, each with an associated score.
- Multiple libraries may have the same book, but each book is scanned only once.

**Libraries:**
- L libraries each with a set of books, a signup duration, and a daily scanning capacity.

**Time:**
- D days available for scanning, starting from day 0 to D-1.

**Library Signup:**
- Libraries must be signed up before scanning.
- Only one signup process can run at a time, and libraries may be signed up in any order.

## Input Data Set Format

Plain-text files delimited by newline characters.

- **First line:** Total books (B), libraries (L), days (D).
- **Second line:** Scores for each book (S[0] to S[B-1]).

For each library (L sections):

- **First line:** Number of books (N), signup duration (T), books per day (M).
- **Second line:** Book IDs (ID[0] to ID[N-1]).

## Output Data Set Format

Plain-text files delimited by newline characters.

- **First line:** Total number of signed-up libraries.

For each library:

Library ID and number of scanned books: The ID of the library followed by the count of books to be scanned.
Book IDs: IDs of the books to be scanned, listed in the order they will be processed.

## Scores for each algorithm, for each file
| Algorithm / File           | A | B | C | D | E | F |
|---------------------|---|---|---|---|---|---|
| Greedy              | 21 | 9000000 | 5645747 | 4815395 | 7616025 | 5561306 |
| Simulated Annealing | 21 | 5581800 | 894135 | 1288950 | 813619 | 950410 |
| Hill Climbing       | 21 | 1694800 | 115041 | 13975 | 366151 | 948113 |
| Genetic Algorithm   | 21 | 8700000 | 982711 | 4359095 | 2736447 | 1544906 |
