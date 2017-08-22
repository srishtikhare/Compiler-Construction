#!/usr/bin/python3

# SRISHTI KHARE
# ESE GRADUATE STUDENT, FALL 2016
# APPLYING FOR POSITION GRADING/COURSE ASSISTANT FOR COMPILER CONSTRUCTION

import sys

statements = []	#store statements with print and an expression in a list
print_statements = []	#store statements with just print in a list
expressions = []	#store expressions in a list
variables = []	#store variables assignments in a list
labels = []	#store variable names in a list
var = {}	#store variable values
code_flow = {}	#keep track of print statemnt order of occurence in the code

def parse_file(filename):
	#Open file and take inputs from it
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    sub_content = []
    order = 0
    for sub_content in content:
        line_of_code = sub_content.split()
        length = len(line_of_code)
	#store variables, statements, print statements and expressions in lists
        if (line_of_code[0] == "print") and (length == 2):
            order += 1
            code_flow[order] = "print_statements"
            print_statements.append(sub_content)
        elif (line_of_code[0] == "print") and (length > 2):
            order += 1
            code_flow[order] = "statements"
            statements.append(sub_content)
        elif (line_of_code[1] == "=") and (length == 3):
            variables.append(sub_content)
        elif (line_of_code[1] == "=") and (length > 3):
            expressions.append(sub_content)

def exeStatements():
    item = statements.pop(0)
    temp = item.split()
    while '' in temp:
        temp.remove('')	#remove spaces form the statements
    temp.pop(0)
    for i in temp:
        if i in var.keys():
            val = var[i]
            for index in range(0,len(temp)):
                if temp[index] == i:
                    temp[index] = val
	#calculate and print statement resuls, now implemented for limited size
    if len(temp) == 3:
        if temp[1] == '+':
            print(int(temp[0]) + int(temp[2]))
        if temp[1] == '-':
            print(int(temp[0]) - int(temp[2]))
        if temp[1] == '*':
            print(int(temp[0]) * int(temp[2]))
        if temp[1] == '/':
            print(int(temp[0]) / int(temp[2]))
    elif len(temp) == 5:
        if temp[1] == '+':
            temp_result = int(temp[0]) + int(temp[2])
        if temp[1] == '-':
            temp_result = int(temp[0]) - int(temp[2])
        if temp[1] == '*':
            temp_result = int(temp[0]) * int(temp[2])
        if temp[1] == '/':
            temp_result = int(temp[0]) / int(temp[2])

        if temp[3] == '+':
            print(temp_result + (int(temp[4])))
        if temp[3] == '-':
            print(temp_result - (int(temp[4])))
        if temp[3] == '*':
            print(temp_result * (int(temp[4])))
        if temp[3] == '/':
            print(temp_result / (int(temp[4])))


def exePrintStatements():
    item = print_statements.pop(0)	#print values
    temp = item.split()
    print(temp[1])

def exeExpressions():
    item = expressions.pop(0)
    temp = item.split()
    labels.append(temp[0])
    while '' in temp:
        temp.remove('')	#remove spaces form the expressions
    remaining = len(temp)-2
	#calculate and print expression result, now implemented for limited size
    if remaining == 3:
        if temp[3] == '+':
            result = int(temp[2]) + int(temp[4])
        if temp[3] == '-':
            result = int(temp[2]) - int(temp[4])
        if temp[3] == '*':
            result = int(temp[2]) * int(temp[4])
        if temp[3] == '/':
            result = int(temp[2]) / int(temp[4])
    var[labels.pop()] = result

def exeVariables():
    item = variables.pop(0)	#assign variable values
    temp = item.split()
    while '' in temp:
        temp.remove('')
    labels.append(temp[0])
    result = int(temp[2])
    var[labels.pop()] = result

if __name__ == "__main__":

    argument = sys.argv[1:] #take filename as command line argument

    filename = argument[0]

    parse_file(filename)	#parse the file that user entered

    exeVariables()	#first calculate variable result
    exeExpressions()	#second calculate expression result
	#based on the order of occurence in the code, execute print statements
    for key in code_flow:
        if code_flow[key] == "statements":
            exeStatements()
        elif code_flow[key] == "print_statements":
            exePrintStatements()  
#NOTE: At the end of execution of the code, the lists are all empty (sanity check)

