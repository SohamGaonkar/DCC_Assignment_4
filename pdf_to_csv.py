import fitz
import pandas as pd

def convert(filename):
    doc = fitz.open("pdf_data/"+filename+".pdf")
    page_df_lst=[]
    for page in doc:
        tables = page.find_tables()
        table = tables[0]
        page_df = table.to_pandas()
        page_df_lst.append(page_df)

    df = pd.concat(page_df_lst)
    df.to_csv(f"csv_data/{filename}.csv",index =False)
    return  

filename = "EB_Purchase_Details"
convert(filename)
filename = "EB_Redemption_Details"
convert(filename)

