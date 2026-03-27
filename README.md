# CSCI311-DNA-Sequencing-Project
by William Chastain, Jackson Greninger, Laura Ozoria, Cynthia Pintado

HOW TO RUN
----------
1. Clone the repository
2. Run: python3 GUI.py

HOW TO USE
----------
1. Click "Start" on the Welcome page.
2. Select your Query file and DNA Sequences file.
3. Pick an algorithm from the dropdown menu.
4. Click "Continue" to run and see the results of the algorithm.
5. Click "Back" to return and try a different algorithm.

INPUT FILE FORMAT
-----------------
DNA Sequences files must be plain .txt files in FASTA format.

ALGORITHMS
----------
- Longest Common Substring: finds the longest consecutive matching 
  characters between the query and each database sequence.

- Longest Common Subsequence: finds the longest matching sequence of
  characters in the same order.

- Needleman-Wunsch: scores the overall alignment between the query
  and each database sequence.

GUI ERRORS:
-------------------------
Our project uses the tkinter Python Library to set up the GUI.
There is a chance that you might not have this library downloaded:

   - Linux :  sudo apt-get install python3-tk
  -  MACOS:            brew install python-tk
   - Windows: python should aready include tkinter, otherwise use pip install tkinter