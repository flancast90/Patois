# ParPy: A python natural language
# parser based on the one used
# by Zork, for use in Python games

# Copyright (c) Finn Lancaster 2021

# This file contains the example usage
# of the ParPy repo

from Patois import *

def mainFunction():
    inp = input("Enter a command (Ex. Hit James) or (Ex. Hit James with ...)\n")
    print(ParPy(inp))   
    mainFunction()

mainFunction()

