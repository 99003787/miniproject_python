# importing the module 
import pandas 
  
# reading the files 
f1 = pandas.read_excel("registration details.xlsx") 
f2 = pandas.read_excel("exam results.xlsx") 
  
# merging the files 
f3 = f1[["REGISTRATION NO",  
         "STUDENT EMAIL ID "]].merge(f2[["REGISTRATION NO",  
                                         "Name", "Marks Obtained",  
                                         "Percentage"]],  
                                     on = "REGISTRATION NO",  
                                     how = "left") 
  
# creating a new file 
f3.to_excel("Results.xlsx", index = False) 

//second
import pandas as pd
import numpy as np
all_data = pd.DataFrame()
for f in glob.glob("../in/sales*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    all_data.describe()
    status = pd.read_excel("../in/customer-status.xlsx")
    all_data_st = pd.merge(all_data, status, how='left')
all_data_st.head()
all_data_st[all_data_st["account number"]==737550].head()
all_data_st['status'].fillna('bronze',inplace=True)
all_data_st.head()
all_data_st["status"].cat.set_categories([ "gold","silver","bronze"],inplace=True)

