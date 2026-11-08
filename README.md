# CSCE-4110-Algorithms
## Longest Common Subsequence (LCS)Explorer

Author: Sikono Williams Shonibare

## Project Description
An interactive python algorithm that shows how the Longest Common Subsequence problem is solved with dynamic programming. You type in two strings, and the algorithms build the DP table, shows how each cell was computed, and traces back to one valid LCS.

## What is LCS?
The LCS of two strings is the longest sequence of characters that appears in both, in the same order. The character do not need to be next to each other; that is what makes it a subsequence not substring.
EXAMPLE: X=CBABDAB, Y=BDCABA->one LCS is CABA. (length 4)

## Why dynamic programming?
A brute-force solution checks every possible subsequence, which is very slow with a time complexity of O(2ᵐ).

Dynamic Programming is more efficient because it stores and reuses previous results instead of solving the same subproblems repeatedly. By filling a table once, it finds the LCS in O(m × n) time using O(m × n) space.

## How does it work?
- `dp[i][j]` = LCS length of the first `i` characters of X and the first `j` characters of Y.
- **Base case:** `dp[0][j] = 0` and `dp[i][0] = 0` (an empty string has no common characters).
- **Match** (`X[i] == Y[j]`): `dp[i][j] = dp[i-1][j-1] + 1` (diagonal + 1)
- **Mismatch:** `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (best of top and left)
The answer is in `dp[m][n]`. Trace back from there to recover an actual LCS.
 
## Features
- Input validation (no empty strings, size limit)
- Bottom-up DP solver
- Full table display with match / mismatch highlighting
- Step-by-step explanation of each cell (top, left, or diagonal)
- Traceback path to rebuild one LCS
- Brute-force checker for small inputs
- Longest common substring comparison
- Runtime and cell-count measurement to confirm O(mn) growth
- Stretch goals: memoized and space-optimized versions

## Setup
1. Install Python 3.8 or newer from https://www.python.org (Tkinter is included on Windows and macOS installers).
2. Clone the repository:
```
   git clone <your-repo-url>
   cd lcs_explorer
```
 
3. On some Linux systems Tkinter must be installed separately:
```
   sudo apt install python3-tk
```
## Dependencies
 
- Python 3 standard library only (`tkinter`, `itertools`, `time`, `random`, `string`, `unittest`)
- No third-party packages, no external datasets, no API keys
## How to Run
 
```
python main.py
```
 
Run the tests:
 
```
python -m unittest discover tests
```
 
## Example Usage
 
1. Run `python main.py`.
2. Enter X = `CBABDAB` and Y = `BDCABA`, then click **Solve**.
3. The DP table appears and the LCS length is 4.
4. Step through cells to see the match rule and mismatch rule.
5. The traceback path is highlighted and an LCS is shown (for example `CABA`).

## References
 
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C. (2009). *Introduction to Algorithms* (3rd ed.), Section 15.4. MIT Press.
- Python Software Foundation. tkinter documentation. https://docs.python.org/3/library/tkinter.html
- CSCE 4110 Week 6 lecture slides: Dynamic Programming Applications. 
