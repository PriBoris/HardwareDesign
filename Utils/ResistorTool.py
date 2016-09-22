
"""Resistor Tool

1.Enter necessary resistor value in ohms
2.Choose row {E6,E12,E24,E48,E96,E192}
3.See results



"""

e6Row = (1.0,1.5,2.2,3.3,4.7,6.8)


def powerRow():
    return (0.001,0.01,0.1,1,10,100,1000,10000,100000)

def rGenerator(row):
     for r in row:
        for p in powerRow():
            yield r*p    


def getStandAlone(targetR,row):
    bestR = 0
    bestAbsError = float("+Inf")
    bestError = float("+Inf")
    for testR in rGenerator(row):
        testError = (testR-targetR)/targetR*100.0
        testAbsError = abs(testError)
        if (testAbsError<bestAbsError):
            bestR = testR
            bestError = testError
            bestAbsError = testAbsError

    result = dict()
    result["r"] = bestR
    result["err"] = bestError
    result["absErr"] = bestAbsError
    return result

def getSeries2(targetR,row):
    bestR = 0
    bestR1 = 0
    bestR2 = 0
    bestAbsError = float("+Inf")
    bestError = float("+Inf")
    for testR1 in rGenerator(row):
        for testR2 in rGenerator(row):
            testR = testR1+testR2
            testError = (testR-targetR)/targetR*100.0
            testAbsError = abs(testError)
            if (testAbsError<bestAbsError):
                bestR = testR
                bestR1 = testR1
                bestR2 = testR2
                bestError = testError
                bestAbsError = testAbsError

    result = dict()
    result["r"] = (bestR1,bestR2)
    result["r*"] = bestR
    result["err"] = bestError
    result["absErr"] = bestAbsError
    return result

def getParallel2(targetR,row):
    bestR = 0
    bestR1 = 0
    bestR2 = 0
    bestAbsError = float("+Inf")
    bestError = float("+Inf")
    for testR1 in rGenerator(row):
        for testR2 in rGenerator(row):
            testR = 1/(1/testR1+1/testR2)
            testError = (testR-targetR)/targetR*100.0
            testAbsError = abs(testError)
            if (testAbsError<bestAbsError):
                bestR = testR
                bestR1 = testR1
                bestR2 = testR2
                bestError = testError
                bestAbsError = testAbsError

    result = dict()
    result["r"] = (bestR1,bestR2)
    result["r*"] = bestR
    result["err"] = bestError
    result["absErr"] = bestAbsError
    return result
    




print("Resistor Tool:")
print()

minTargetR = 0.001
maxTargetR = 1000000

try:
    targetR = float(input("Enter necessary resistor value in ohms:"))
    if targetR<minTargetR:
        print("value shoulnt be less than",minTargetR)
        raise
    if targetR>maxTargetR:
        print("value shoulnt be greater than",maxTargetR)
        raise
    
except:
    print("You entered bad value")
    raise SystemExit


print("Stage1:","seeking best stand alone resistor")
print(getStandAlone(targetR,e6Row))

print("Stage2:","seeking best series2 resistor")
print(getSeries2(targetR,e6Row))
    
print("Stage3:","seeking best parallel2 resistor")
print(getParallel2(targetR,e6Row))
    







