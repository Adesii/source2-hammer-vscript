import json

file = open("AllData.json","r")
x = json.loads(file.read())

count = 0

cleaned = {}

for function in x:
    eachfunction=0
    cleaned[count] = {}
    for name in function:
        cleaned[count][eachfunction] =name
        eachfunction+=1
        
    count+= 1
    pass

finalSnippets={}

for function in cleaned:
    try:
        name= cleaned[function][0]
        cleanedFunction = cleaned[function][1].replace("("," ( ").replace(")"," )")
        subbedFunction = cleanedFunction.split()
        returntype = subbedFunction[0]
        finalSnippets[name] ={}
        finalSnippets[name]["prefix"] = name
        start = False
        index = 0
        newBuildFunction=subbedFunction[1]+"("
        for subfunc in subbedFunction:
            if(subfunc == ")"):
                start=False
            if(index % 2 == 0):
                if(start):
                    newBuildFunction+= "${"+str(index)+":"+str(subfunc)+"}"

            index +=1
            if(subfunc == "("):
               start=True
            pass
        finalSnippets[name]["body"] = newBuildFunction.replace(",","").replace("}$","},$")+")"
        try:
            finalSnippets[name]["description"] = cleaned[function][1]+ cleaned[function][2]
            pass
        except:
            finalSnippets[name]["description"] = cleaned[function][1]
            pass
    except:
        pass
    

jsonfile = open("data.json","w")

jsonfile.write(json.dumps(finalSnippets))