# Cleaning the csv file
import pandas as pd
# to remove unnecesasry newline characters from the table headers 
df=pd.read_csv("csv_data/EB_Redemption_Details.csv")
print(df.columns)
df.rename(columns={'Date of\nEncashment':'Date of Encashment', 'Account no. of\nPolitical Party':'Account no. of Political Party','Bond\nNumber':'Bond Number','Pay Branch\nCode':'Pay Branch Code'},inplace=True)
print(df)
df.to_csv("csv_data/EB_Redemption_Details.csv",index=False)

df=pd.read_csv("csv_data/EB_Purchase_Details.csv")
print(df.columns)
df.rename(columns={'Date of\nPurchase':'Date of Purchase','Bond\nNumber':'Bond Number'},inplace=True)
print(df)
df.to_csv("csv_data/EB_Purchase_Details.csv",index=False)