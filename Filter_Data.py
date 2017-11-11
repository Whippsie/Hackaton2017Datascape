#vehicules-circulation-2016 dataset
#dataset link - https://saaq.gouv.qc.ca/donnees-ouvertes/vehicules-circulation/vehicules-circulation-2016.csv
#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df = pd.DataFrame()

################ Reading data #################################################################################
#read_csv from pandas will read the csv file into dataframe(which is table like format)
df = pd.read_csv('vehicules-circulation-2016.csv')


#number of records in dataset
lenDf = len(df)
print("Number of records: "+str(lenDf))


print("###### Filtering on values of column ######")
#filters the records in which MARQ_VEH has value - HONDA
dfPhysical = df[df["TYP_DOSS_PERS"] == "P"].copy()
dfMoral = df[df["TYP_DOSS_PERS"] == "M"].copy()

lenDfMoral = len(dfMoral)
print("Number of records: "+str(lenDfMoral))
print("Number of records: "+str(lenDf- lenDfMoral))


'''
print("####### Multiple filters on column and get value of other column ########")
#Gives value of PHYS_SEX column where COUL_ORIG is BLA and NB_CYL is 4.0
print(df.loc[(df["COUL_ORIG"]=="BLA")&(df["NB_CYL"]== 4.0),"PHYS_SEX"])
'''
