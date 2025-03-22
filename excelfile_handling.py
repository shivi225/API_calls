import pandas as pd
file_path = "excel.xlsx"
try:
    df=pd.read_excel(file_path,sheet_name = "Sheet1")
    print(df)
    print(df.head())
except Exception as e:
    print("Error",e)


#--------------------------------#
#writing into excel 
data={
    'S NO':[1,2],
    'Item':['item1','item2'],
    'Status':['Pass','Nk'],
    'Reason':['Reason1','Reason2']
    }
#imp to note that give the value in list format other wise it will fail
df=pd.DataFrame(data)
df.to_excel("excel.xlsx",index=False)
#index=True/False : it creates extra column with index

df=pd.read_excel("excel.xlsx",sheet_name='Sheet1')
print(df['S NO'])  #if we wnat to get data of any column
st_value = df.loc[0, 'Status']  #first row of status value
print(st_value)
#----------------------------#
#above was writing data from start everytime it will over right the existing data
#concaticate teh data
#pd.concat
data={
    "S NO":[3],
    "Item":['item3'],
    "Status":['AMBER'],
    "Reason":["Reason4"]
    }
df2=pd.DataFrame(data)
# df2.to_excel("excel.xlsx",index=False)  #this will overright the data
data=pd.concat([df,df2],ignore_index=True)
data.to_excel("excel.xlsx",index=False)  #we can save data to same or diff file also

#update specifc column value :
data.loc[data['Reason']=='Reason2','Status'] = 'Done'
data.to_excel("excel.xlsx",index=False)

#Delete the row
data.drop(index=2)
data.to_excel("excel.xlsx",index=False)