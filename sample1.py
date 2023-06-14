import json

with open(r"C:\Users\vidyashree.v\PycharmProjects\pythonProject44\sample_data (1).json",) as myfile:
    f = myfile.read()
val = json.loads(f)

print(val)
list_1=[]
details=val["parametersList"]

for para in details:
    dict = {}
    details1=para['parameterName']

    details2=para['max']
    details3=para['min']
    details4=para['avg']

    dict['parameterName']=para["parameterName"]
    dict['min_value']=para["min"]
    dict['max_value']=para["max"]
    dict['avg_value']=para['avg']

    list_1.append(dict)
print(list_1)
with open("C://Users//vidyashree.v//PycharmProjects//pythonProject44//sample.json","w") as myfile :
    details=myfile.write(json.dumps(list_1, indent=2))
    print(details)

























