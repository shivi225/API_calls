import requests as req
import json
res= req.get("https://reqres.in/api/users/2")
print(res.status_code) #code 200 is successful
data=res.json()
print(data)
for key,value in data['data'].items():
    print(key,": ",value)

#----------------------#
#GET : for getting the requested resource
res=req.get("https://reqres.in/api/users/23")
try:
    x=res.status_code
    if x ==200:
        print(res.json())
    else:
        print("Error Code : ",x)
        #404 : data not found
except Exception as e:
    print("Error",e)

#------------------------#
# POST 
#For creating the new resource
new_data={
    "name": "morpheus",
    "job": "leader",
    "id": "584",
    "createdAt": "2025-03-21T05:08:17.642Z"
}
res=req.post(url="https://reqres.in/api/users",json=new_data)
print(res.status_code)
if res.status_code ==201:
    print("Data posted successfully")
    print(res.json())
else:
    print("Error",res.status_code)

#--------------------------------#
#PUT
#PUT: for modifying the existing resource completely
updated_data={
    "name": "morpheus",
    "job": "zion resident",
    
}
res=req.put(url="https://reqres.in/api/users/2",json=updated_data)
print(res.status_code)
if res.status_code==200:
    print("data is changed successfully")
    print(res.json())
else:
    print("Error",res.status_code)

#----------------------------------#
#PATCH
#PATCH : update data partially
updated_data= {
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2025-03-21T05:33:23.143Z"
}
res=req.patch(url="https://reqres.in/api/users/2")#,json=updated_data)
if res.status_code ==200:
    print("Done")
    print(res.json())
else:
    print("Error",res.status_code)
    