import json

f = open('/mnt/c/Users/Asus/OneDrive/Desktop/count/jsonformatter.json') #json file


data = json.load(f)
count = 0
#for i in data['paths']:
    
	#apiList = i
    #apiMethod = json.dumps(data['paths'][apiList])
    #apiMethodJson = json.loads(apiMethod)
    #for i in apiMethodJson:
     #   if(i!='parameters'):
      #      print(i+' '+apiList)
    
    #print(i)
    
for i in data['paths']:
    apiList = i
    apiMethod = json.dumps(data['paths'][apiList])
    apiMethodJson = json.loads(apiMethod)
    for i in apiMethodJson:
        if(i!='parameters'):
            count = count+1
            print(i+' '+apiList)

print("Total: " + str(count))    
f.close()