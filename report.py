import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_excel(r"flight_Train.xlsx",engine='openpyxl')
'''due to less security feature pandas not support excel file hence
 have to add external reader and then able to read xlsx file '''
print (df)

#generate a report
profile = ProfileReport(df)
profile.to_file(output_file = "report_airline.html")