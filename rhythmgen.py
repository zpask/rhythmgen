import random

def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer

values = {1: "sixteenth", 2: "eighth", 3: "dotted eighth", 4: "quarter", 5: "quarter tied to sixteenth", 6: "dotted quarter", 7: "double-dotted quarter", 8: "half", 9: "half tied to sixteenth", 10: "half tied to eighth", 11: "half tied to dotted eighth", 12: "dotted half", 13: "dotted half tied to sixteenth", 14: "double-dotted half", 15: "triple-dotted half", 16: "whole"}

n = True
while n == True:
    
    top = raw_input("What is the top number of your time signature?\n")
    
    bottom = raw_input("What is the bottom number of your time signature?\n")
    weird = raw_input("Would you like to see weird values eg; half tied to sixteenth? y/n \n")
    if weird == "y":
        weird = True
    elif weird == "n":
        weird = False
    
    print ""
    
    top = int(top) + 0.0
    
    bottom = int(bottom) + 0.0
    
    workingvalue = (top/bottom)/(0.0625)
    
    workingvalue = int(workingvalue)
    
    wvresult = partition(workingvalue)

    
    if weird == True:
        result = random.sample(wvresult, 1)
        resultlist = result[0]
    
    else:
        weirdness = True
        while weirdness == True:
            result = random.sample(wvresult, 1)
        
            resultlist = result[0]
    		
            if weird == False:
                if 5 in resultlist or 7 in resultlist or 9 in resultlist or 10 in resultlist or 11 in resultlist or 13 in resultlist or 14 in resultlist or 15 in resultlist:
                    weirdness = True
                else:
    		        weirdness = False
    
    thing = list(resultlist)
    
    shuffled = random.shuffle(thing)
    
    print thing
    
    print ""
    for integer in thing:
        print values[integer]
    print ""
    
    whatever = raw_input("Press enter to generate another. Enter 'q' to quit.")
    print ""
    if len(whatever) > 0:
        n = False
