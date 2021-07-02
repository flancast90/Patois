# ParPy: A python natural language
# parser based on the one used
# by Zork, for use in Python games

# Copyright (c) Finn Lancaster 2021

# This file contains the BASE action words
# accepted by the users program. For example
# , take, move, etc.
# ParPy handles similar entries and conversion
# to program-accepted ones

# in parentheses, the first field is the word
# and the second field is whether or not the 
# word needs something to do it with (yes or no)
recognizedTerms = [("hit","yes"),("attack","yes"),("grab","no"),("move","no")]
