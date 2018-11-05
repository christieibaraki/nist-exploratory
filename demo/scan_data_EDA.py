# packages
import pandas as pd
import re
from datetime import date
import os
from scipy import stats


# import and clean data
filepath = os.path.abspath("../CDM-Data-Model/main/resources/CreatedData.xlsx")

scanFile = pd.read_excel(filepath,
                         sheet_name = "Scan",
                        na_values = ["", " ", "N/A", "nan"])

# first look
print("Head:\n",scanFile.head())
print("# unique:\n", scanFile.nunique())
print("Describe:\n", scanFile.describe())
print("Info:\n", scanFile.info())
# Severity, Protocol, and Exploit look to be categorical.
# we also need to clean up the column names and fix the protocol field

# fix column names
origCols = scanFile.columns


def colNameClean(name):
    '''function to sort of clean up column names, needs improvement'''
    camelcase = name[0].lower() + name[1:].replace(" ","")
    return re.sub(r'\W+', '', camelcase)


# reassign column names
scanFile.columns = [colNameClean(x) for x in origCols]
print(scanFile.columns)

# time since discovered/last obs date
scanFile['daySinceDiscover'] = scanFile.apply(lambda x: (date.today() - x['firstDiscovered'].date()).days, axis = 1)
scanFile['daySinceLastObs'] = scanFile.apply(lambda x: (date.today() - x['lastObservedDate'].date()).days, axis = 1)

# protocol filed has a mix of upper and lower case
scanFile['protocol'] = scanFile.protocol.apply(lambda x: x.upper())

def udpSpell(string):
    '''correct misspelling of UPD to UDP'''
    if string == 'UPD':
        return 'UDP'
    else:
        return string


scanFile['protocol'] = scanFile.protocol.apply(lambda x: udpSpell(x))
print(pd.crosstab(scanFile.protocol2, scanFile.protocol))

# print tables
print("severity table:\n", scanFile.severity.value_counts())
print("protocol table:\n", scanFile.protocol.value_counts())
print("exploit table:\n", scanFile.exploit.value_counts())

print(scanFile.protocol.toupper().value_counts())

# cross tabs and tests of independence
print("Severity and Protocol:\n", pd.crosstab(scanFile.severity, scanFile.protocol))
print("Severity and Exploit:\n", pd.crosstab(scanFile.severity, scanFile.exploit))

