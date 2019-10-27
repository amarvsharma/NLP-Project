import dialogflow_v2 as dialogflow
import os
from google.protobuf.json_format import MessageToDict
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ****
project_id = *****
session_id = *****
language_code = "en"
session_client = dialogflow.SessionsClient()
session = session_client.session_path(project_id, session_id)

def detectReturnType(returnType) -> str:
    r = ''
    if (returnType != ""):
        if (returnType == "integer"):
            r = " -> int:"
            
        elif (returnType == "boolean"):
            r = " -> bool:"
            
        elif (returnType == "array"):
            r = " -> [int]:"
            
        elif (returnType == "string"):
            r = " -> str:"
        else:
            r = ""
    return r

def addInputArrayType(inp):
    return ": [" + (inp if inp != '' else "int") + "]"

def createArrayName(num):
    name = "array"
    name += str(num)
    return name


def detectType(inputType):
    if inputType == "boolean":
        return "bool"
    elif inputType == "int" or inputType == "integer":
        return "int"
    elif inputType == "string":
        return "str"


def createParameterName(num, inputType):
    name = detectType(inputType)
    name += str(num)
    return name


def createDeclarationString(parametersOrNot, inputParam, returnType) -> str:
    numInputStrings = 0
    paramNum = 1
    declaration = "def aMethod("

    if (parametersOrNot != ''):
        if (parametersOrNot == 'Given a'):
            numInputStrings = 1
        else:
            numInputStrings = parametersOrNot[-1:]

        for i in range(0, int(numInputStrings)):
                if (i == int(numInputStrings) - 1):
                    declaration += createParameterName(paramNum, inputParam) + ": " + detectType(inputParam)
                    paramNum +=1
                else:
                    declaration += createParameterName(paramNum,inputParam) + ": " + detectType(inputParam) + ", "
                    paramNum +=1

    declaration += ")"
    
    r = detectReturnType(returnType)
    declaration += (r if r != '' else detectReturnType(inputParam))

    return declaration



def createDeclarationList(parametersOrNot, inputArray, returnType) -> str:
    arrayNum = 1
    declaration = "def listMethod("
    numInputArrays = 0

    if (parametersOrNot != ""):
        if (parametersOrNot == "Given a"):
            numInputArrays = 1
        else:
            numInputArrays = parametersOrNot[-1:]

 
        for i in range(0, int(numInputArrays)):
            if (i == int(numInputArrays) - 1):
                declaration += createArrayName(arrayNum) + addInputArrayType(inputArray)
                arrayNum +=1
            else:
                declaration += createArrayName(arrayNum) + addInputArrayType(inputArray) + ", "
                arrayNum +=1
            
    declaration += ")" 
    declaration += detectReturnType(returnType)
            
    return declaration

#def createDeclarationWarmup():

    
            

def fromFileAndPrint(line):
    line_input = dialogflow.types.TextInput(text=line, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=line_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    rDict = MessageToDict(response.query_result)

    params = rDict['parameters']

    parametersOrNot = params['parametersOrNot']
    returnType = params['returnType']
    #inputParam = params['inputParam']

    ret = ''
    l = 0
    
    if (rDict['intent']['displayName'] == 'list'):
        l = 1
        inputArray = params['inputArray']
        
        if parametersOrNot == '' and inputArray != '':
            #print('---------------------special')
            if "in the array" in line or "of an array of ints" in line:
                parametersOrNot = "Given a"
                
        ret = createDeclarationList(parametersOrNot, inputArray, returnType)
        print(1, ret)
       


    elif (rDict['intent']['displayName'] == 'string'):
        l = 2
        inputParam = params['inputParam']
        ret = createDeclarationString(parametersOrNot, inputParam, returnType)
        print(2, ret)

       

    
def checkError(line):
    if line[0:2] == "!!":
        print("ERROR", line[2:])
        return True
    return False


def main():
    print('FIX STRING1')
    print("Code: 1 (array)")
    print("      2 (string)")
    print('-----List1-----')

    List1 = open("allTextList1.txt", "r")
    for line in List1:
        if (not checkError(line)):
            fromFileAndPrint(line)
    List1.close()

    print("-----String1 (11)-----")
     
    String1 = open("allTextString1.txt", "r")
    for line in String1:
        if (not checkError(line)):
            fromFileAndPrint(line)
    String1.close()

    print("-----String2-----")


    String2 = open("allTextString2.txt", "r")
    for line in String2:
        if (not checkError(line)):
            fromFileAndPrint(line)
    String2.close()

    print('-----List2-----')
    List2 = open("allTextList2.txt", "r")
    for line in List2:
        if (not checkError(line)):
            fromFileAndPrint(line)
    List2.close()

    print('-----Warmup1-----')
    Warmup1 = open("allTextWarmup1.txt", "r")
    for line in Warmup1:
        if (not checkError(line)):
            fromFileAndPrint(line)
    Warmup1.close()

    print('-----Warmup2-----')
    Warmup2 = open("allTextWarmup2.txt", "r")
    for line in Warmup2:
        if (not checkError(line)):
            fromFileAndPrint(line)
    Warmup2.close()


    
    

if __name__ == "__main__":
    main()






