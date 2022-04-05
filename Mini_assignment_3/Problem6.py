sampleDict = {

  "name": "Kelly",

  "age":25,

  "salary": 8000,

  "city": "New york"

}
sampleDict["location"] = sampleDict["city"]
del sampleDict["city"]
print(sampleDict)