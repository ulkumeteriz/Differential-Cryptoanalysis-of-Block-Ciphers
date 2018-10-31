import math
import sys
from sets import Set

Sboxes = [  list("086D5F7C4E2391BA"),
            list("FC27905A1BE86D34"),
            list("86793CAFD1E40B52"),
            list("B94E0FAD6C573812"),
            list("E4B238091A7F6C5D"),
            list("7A2C48F0591E3DB6"),
            list("72C5846BE91FD3A0"),
            list("14BDC37EAF680592"),
            list("0A4FC728DE9B5631") ]


def reverseSBox ( sbox ) :
    i = 0
    result = []
    while i < len(sbox):
        char = hex(i).upper()[2:]
        result.append(hex(sbox.index(char)).upper()[2:])
        i = i + 1
    return result

def createEmptyList(size):
    return [0]*size

def createEmpty2DList(size):
    result = []
    x = 0
    while x < size:
        result.append(createEmptyList(size))
        x += 1
    return result

def generatePairsWithDifference( diff ):
    result = []
    for x in range (0,16):
        for y in range (0,16):
            if x ^ y == diff:
               result.append((x,y))
               break 
    return result
    
def outputDifferenceOfPairOverloaded(pair, SBox):
    firstOutput = SBox[pair[0]]
    secondOutput = SBox[pair[1]]
    firstOutput = int(firstOutput, 16)
    secondOutput = int(secondOutput, 16)
    return firstOutput ^ secondOutput

def outputDifferenceOfPair(pair, SBoxes, SBoxNumber):
    firstOutput = SBoxes[SBoxNumber][pair[0]]
    secondOutput = SBoxes[SBoxNumber][pair[1]]
    firstOutput = int(firstOutput,16)
    secondOutput = int(secondOutput, 16)
    return firstOutput ^ secondOutput

def printDDT( DDT ):
    print "\t|0\t1\t2\t3\t4\t5\t6\t7\t8\t9\tA\tB\tC\tD\tE\tF"
    print "----------------------------------------------------------------------------------------------------------------------------------"
    
    k = 0
    while k < len(DDT):
        s = str(k) + "\t|"
        for i in DDT[k]:
            s = s + "" + str(i) + "\t"
        print s
        k = k + 1

def DDT(SBoxes, SBoxNumber):
    DDT = createEmpty2DList(16)
    differentialUniformity = 0   
    for x in range(0,16):
        pairs = generatePairsWithDifference(x)
        for pair in pairs:
            diff = outputDifferenceOfPair(pair, SBoxes, SBoxNumber)
            DDT[x][diff] += 1
            if x != 0 and DDT[x][diff] > differentialUniformity:
                differentialUniformity = DDT[x][diff]
    print "\nDifferential Uniformity of SBox" + str(SBoxNumber) + " : " + str(differentialUniformity)
    return DDT


def findReverseSBoxes(SBoxes):
    inverseSBoxes = []
    for sbox in SBoxes:
      inverseSBoxes.append(reverseSBox(sbox))
    return inverseSBoxes
      
def printSBoxes( SBoxes, typ ):
    print "\t0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F"
    print "---------------------------------------------------------------------"
    for sBox in SBoxes:
        print typ + "_" + str(SBoxes.index(sBox)) + "\t" + " | ".join(sBox)
    print "---------------------------------------------------------------------"

def printAllDDT( SBoxes, typ ):
    for i in range(0,9):
        print "#### Differential Distribution Table of " + typ + "SBox-" + str(i) + " ####"
        printDDT(DDT(SBoxes, i))
        print "\n"

#########################################################################################################3

def getNonZeroIndexes( L ):
    result = []
    i = 0
    while i < len(L) :
        if L[i] != 0:
            result.append(i)
        i += 1
    return result

## result [ [ [ ] ] ]
def getOutputDifferencesSet(SBoxes):
    s = 0
    result = []
    while s < len(SBoxes):
        ddt = DDT(SBoxes, s)
        resultOfOneSBox = []
        for l in ddt:
            resultOfOneSBox.append(getNonZeroIndexes(l))
        result.append(resultOfOneSBox)
        s += 1
    return result

## outputDiffSet [ [ ] ]    
def getUndisturbedBitsOfAnSBox( outputDiffSet ):
    i = 0
    while i < len(outputDiffSet):
    
        undisturbed = []
        
        ORresult = 0b0000
        ANDresult = 0b1111
        
        for j in outputDiffSet[i]:
            ORresult = ORresult | j
            ANDresult = ANDresult & j
            
        XORresult = ORresult ^ ANDresult
        
        binaryRep = list(bin(XORresult)[2:])
        
        # 0s in XORresult are undisturbed bits
        c = 0
        while c < len(binaryRep):
            if binaryRep[c] == '0':
                undisturbed.append(c)
            c += 1
        
        if len(undisturbed) > 0 :
            print "Indexes of undisturbed bits for " + str(i) + " input difference: "
            print undisturbed
        
        i += 1
    
def determineUndisturbedBitsOfSBoxes(SBoxes):
    outputDifferences = getOutputDifferencesSet(SBoxes)
    ## output [ [ ] ]
    for output in outputDifferences:
        print "\n#### Undisturbed bits for SBox" + str(outputDifferences.index(output)) + " :"
        getUndisturbedBitsOfAnSBox(output)
        
def findLambdaAndMuForSBoxes( sBoxes ):
    i = 0
    for sBox in sBoxes:
        print "############  S-Box" + str(i) + "  ############"
        findLambdaAndMuForSBox( sBox )
        i += 1
        

def findLambdaAndMuForSBox( sBox ):
    result = Set()
    for diff in range(1,16):
        print "#### For input difference " + str(diff)
        pairs = generatePairsWithDifference(diff)
        
        for pair in pairs:
            Mu = outputDifferenceOfPairOverloaded(pair,sBox)
            
            for Lambda in range(1,16):
                firstElement = pair[0] ^ Lambda
                secondElement = pair[1] ^ Lambda
                newPair = (firstElement, secondElement)
                newMu = outputDifferenceOfPairOverloaded(newPair,sBox)
                if newMu == Mu:
                    result.add((str(Lambda),str(Mu)))
        
        for r in result:
            print "Lambda: " + r[0] + " Mu: " + r[1]
        print ""
        
        
def printLAT( LAT ):
    print "\t|0\t1\t2\t3\t4\t5\t6\t7\t8\t9\tA\tB\tC\tD\tE\tF"
    print "----------------------------------------------------------------------------------------------------------------------------------"
    i = 0
    line = ""
    for entry in LAT:
        if i%16 == 0:
            line += str(i/16) + "\t|"
        line += str(entry) + "\t"
        if i%16 == 15:
            line += "\n"
        i += 1
    print line
        
def mask(x, a):
    
    binX = bin(x)[2:]
    binA = bin(a)[2:]
    
    if len(binX) < 4:
        binX = "0"*(4-len(binX)) + binX
    
    if len(binA) < 4:
        binA = "0"*(4-len(binA)) + binA
    
    r = int(binX[0]) & int(binA[0])
    for j in range(1,4):
        r ^= int(binX[j]) & int(binA[j])
    return r
        
def LATofSBOX( sBox ):
    lat = []
    for i in range(0,16):
        for j in range(0,16):
            r = 0
            for x in range(0,16):
                sx = int(sBox[x],16)
                r += (mask(i,x) ^ mask(j,sx))
            r = r - 8
            lat.append(r)
    printLAT(lat)

def LAT(sBoxes):
    i = 0
    while i < len(sBoxes):
        print "######## LAT of SBox-" + str(i) + " ########"
        LATofSBOX( sBoxes[i] )
        print
        i += 1
        

################################# MAIN #############################################3


# reverses and prints SBoxes
if sys.argv[1] == "reverseSBOXES":
    print "#####################  Inverse S-Boxes  #####################"
    ReverseSBoxes = findReverseSBoxes(Sboxes)
    printSBoxes(ReverseSBoxes, "rSBox")
elif sys.argv[1] == "SBOXES":
    print "#########################  S-Boxes  #########################"
    printSBoxes(Sboxes, "SBox")
elif sys.argv[1] == "DDT" : 
    printAllDDT(Sboxes, "")
elif sys.argv[1] == "reverseDDT":
    ReverseSBoxes = findReverseSBoxes(Sboxes)
    printAllDDT(ReverseSBoxes, "reverse ")
elif sys.argv[1] == "UNDISTURBED":
    determineUndisturbedBitsOfSBoxes(Sboxes)
elif sys.argv[1] == "reverseUNDISTURBED":
    ReverseSBoxes = findReverseSBoxes(Sboxes)
    determineUndisturbedBitsOfSBoxes(ReverseSBoxes)
elif sys.argv[1] == "LAMBDAandMU":
    findLambdaAndMuForSBoxes(Sboxes)
elif sys.argv[1] == "reverseLAMBDAandMU":
    ReverseSBoxes = findReverseSBoxes(Sboxes)
    findLambdaAndMuForSBoxes(ReverseSBoxes)
elif sys.argv[1] == "LAT":
    LAT( Sboxes )
elif sys.argv[1] == "reverseLAT":
    ReverseSBoxes = findReverseSBoxes(Sboxes)
    LAT( ReverseSBoxes )





  

