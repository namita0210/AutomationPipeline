import pandas as pd
import re

class Roboto:

    def read_excel_to_dataframe(file_path):

        ''' Enter the path of the file
        in the format (r " ")'''

        try:
            # Read Excel file into a DataFrame
            df = pd.read_excel(file_path )
            print("Excel file successfully read into DataFrame.")
            return df
        except FileNotFoundError:
            print("Error: File not found.")
            return None
        except Exception as e:
            print("Error:", e)
            return None
    
    def preprocess(df):
    
        '''Pass a dataframe as parameter.
        This function is for string data  nan value  handling purpose.
        This function will check for null values. 
        Column with all values equal to null will be dropped.
        Columns with same rows missing will be dropped
        Other columns with unsynced missing rows will be imputed with the string "No value specified" '''

        size = df.shape
        nrows = size[0]

        #calculate null values
        null_values = df.isnull().sum()
        #print("Null values in each column:\n", null_values)

        col_idx = [] # capture index of null values
        for i, n in enumerate(null_values):
            if ((n > 0) & ( n != nrows)): # is null values exist
                col_idx.append(n)      

        col_names = [] # capture names of cols with null values
        for idx in col_idx:
            name = df.columns[idx]
            col_names.append(name)   

        #create dataframe of cols with null values
        dictionary = {}
        for name in col_names:
            dictionary[name] = df[name]      

        df2 = pd.DataFrame(dictionary)    

        # null_rows = df2[dictionary[col_names[0]].isnull() & dictionary[col_names[1]].isnull()]
        null_rows = None

        for col in col_names:
            if null_rows is None:
                null_rows = df2[dictionary[col].isnull()]
            else :
                null_rows = null_rows[dictionary[col].isnull()]    

        # Drop rows where all columns have null values
        if null_rows is not None:
            df2.drop(null_rows.index, inplace=True)        

        df2 = df2.fillna("not specified", inplace=True)    

        df = df.drop(col_names)

        dict_of_lists = df.to_dict(orient='list')

        df3 = pd.DataFrame(dict_of_lists)

        for col, values in dictionary.items():
            df3[col] = values

    def clean_text(text):
        # Convert text to lowercase
        text = text.lower()
        
        # Remove special characters, punctuation, and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text        


