import pandas as pd
 
#data = {"Name" : ["Priya", "john", "Jack"],
        #"Age" : [30, 25, 50],
        #"Salary" : [50000, 30000, 45000]}

data = pd.read_csv("C:/Users/Lenovo/Downloads/archive (1)/Employee.csv")

#print(data.head(10))
#print(data.tail(10))
#print(data.info())
#print(data.describe())
print(data.isnull().sum())
#print(data["City"].duplicated().sum())
print(data.count())