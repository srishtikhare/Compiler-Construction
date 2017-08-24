Compiler Construction Python

This assignment is for the Grader/Course Assistant position for course Compiler Construction course.
The python interpreter code has been written to compile/run statements, expressions and variable assignment containing files.
The code is limited to use of few variants of the inputs, examples of which can be found in files test1.py, test2.py and test3.py.
The python interpreter file is named Compiler_Construction.py.

NOTE: The test files to be run with the python code are to be given as command line arguments, one file at a time of each run.

FUNCTIONS:

parse_file(filename) -- This function reads the input file, identifies the print statements, statements, expressions and variable assignment operations and assigns them to their respective lists for calculations.

exeSttements() -- This function operates upon the statements list and prints out the results

exePrintStatements() -- This function operates upon the print statements list and prints values in the order of their occurence in the file to main the flow.

exeVariables() -- This function operates upon the variables list and performs variable assignment operation.

Main() -- This function executes the parsing of file and, after calculation of expressions, print statements, statements and variable assignment operations, prints the values in the order of occurence in the original file, to maintain the code flow.
