import pandas as pd
import re

class Roboto:

    def read_excel_to_dataframe(self, file_path):

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
    
    def preprocess(self, df):
    
        '''Pass a dataframe as parameter.

        This function is for string data  nan value  handling purpose.

        This function will check for null values. 

        Columns with all values equal to null will be dropped.

        Rows of those columns that have the same rows missing - those rows will be dropped.

        Other columns with unsynced missing rows will be imputed with the string "No value specified" '''

        size = df.shape
        nrows = size[0]

        #calculate null values
        null_values = df.isnull().sum()

        null_vals_dict = null_values.to_dict() # convert null values series to dictionary

        #filter nul_values_dit to get the null_values columns and the number of null values they have except the column where all values are null

        dictionary =   {key: value for key, value in null_vals_dict.items() if value > 0 and value != nrows} 

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

            df2.fillna("not specified", inplace=True)    

        df = df.drop(col_names)

        dict_of_lists = df.to_dict(orient='list')

        df3 = pd.DataFrame(dict_of_lists)

        for col, values in dictionary.items():
            df3[col] = values

        return df3    

    def clean_text(self, text):
        # Convert text to lowercase
        text = text.lower()
        
        # Remove special characters, punctuation, and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text        

# main

