# ParPy: A python natural language
# parser based on the one used
# by Zork, for use in Python games

# Copyright (c) Finn Lancaster 2021

import nltk
from nltk import word_tokenize
from actions import recognizedTerms
from PyDictionary import PyDictionary
from nltk import pos_tag
from nltk.tokenize import RegexpTokenizer

dictionary=PyDictionary()


def ParPy(input_):  
    output = []
    VBP_Tagged = ""
    NN_Tagged = ""
    NNS_Tagged = ""
    doTo_it = "null"
    word_needsObj = "no"
    TOKENIZER = RegexpTokenizer('\w+|[^\w\s]+')
# Make sentence "grammatically correct"
# By adding the implied "you." 
# This is necessary for command-based
# text-games.
    Sentence = TOKENIZER.tokenize("You "+input_)
    POS_Tagged = nltk.pos_tag(Sentence)
    print(POS_Tagged)
    for (word, tag) in POS_Tagged:
        if tag == "NN":
            NN_Tagged = word
        elif tag == "NNS":
            NNS_Tagged = word
        elif tag == "VBP":
            VBP_Tagged = word
            VBP_Synonyms = dictionary.synonym(VBP_Tagged)
            for (word_, needsObj) in recognizedTerms:
                if word_ == VBP_Tagged.lower():
                    VBP_Tagged = VBP_Tagged.lower()
                else:
                    if word_ in VBP_Synonyms:
                        VBP_Synonyms = word_
                        word_needsObj = needsObj
    if VBP_Tagged == "" or NNS_Tagged == "":
        print(VBP_Tagged)
        print(NNS_Tagged)
        if NNS_Tagged == "" and VBP_Tagged != "":
            inp = input("What would you like to "+VBP_Tagged+"?\n")
            ParPy(VBP_Tagged+" the "+inp.replace("the","").replace("The",""))
        elif VBP_Tagged == "" and NNS_Tagged != "":
            inp = input("What would you like to do with the "+NNS_Tagged+"?\n")
            ParPy(inp.replace("it","")+" the "+NNS_Tagged)
        else:
            inp = input("Please enter a valid command.\n")
            ParPy(inp)
    else:
        if NN_Tagged == "" and word_needsObj == "yes":
            inp = input("What would you like to "+VBP_Tagged+" the "+NNS_Tagged+" with?\n")
            ParPy(VBP_Tagged+" the "+NNS_Tagged+" with the "+inp.replace("the",""))
        else:
            doTo_it = NN_Tagged
            output.append(VBP_Tagged)
            output.append(NNS_Tagged)
            output.append(doTo_it)
            return output

    
