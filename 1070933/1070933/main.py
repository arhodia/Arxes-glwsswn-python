import pandas as pd
import matplotlib.pyplot as plt
import gzip
import requests
import shutil
import mysql.connector
#connect and create datbase and tables for each link separate
db=mysql.connector.connect(user="root",password="",host='localhost')
cursor = db.cursor()
cursor.execute("DROP DATABASE IF EXISTS AGP")
cursor.execute("CREATE DATABASE IF NOT EXISTS AGP")
cursor.execute("USE AGP")
cursor.execute("CREATE TABLE IF NOT EXISTS NIGHT(year year(4) NOT NULL, greece FLOAT NOT NULL, spain BIGINT  not null )")
cursor.execute("CREATE TABLE IF NOT EXISTS ARRIVALS(year year(4) NOT NULL, greece FLOAT NOT NULL, spain BIGINT  not null )")
cursor.execute("CREATE TABLE IF NOT EXISTS NIGHT_NON(year year(4) NOT NULL, greece FLOAT NOT NULL, spain BIGINT  not null )")
cursor.execute("CREATE TABLE IF NOT EXISTS ARRIVALS_NON(year year(4) NOT NULL, greece FLOAT NOT NULL, spain BIGINT  not null )")
#visit each url that we are intrested  and parses into variables
url = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz'
url1= 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00174.tsv.gz'
#function that  download files from the web and filtering the data
def download_file(url, file1, file2):
    r = requests.get(url, allow_redirects=True)
    open(file1, 'wb').write(r.content)
    with gzip.open(file1, 'rb') as f_in:      #Decompress gzip File
        with open(file2, 'wb') as f_out:      #convert gz in txt
            shutil.copyfileobj(f_in, f_out)

    df = pd.read_csv(file2, sep='\t', header=0)      #read the file as csv keeps only the columns and rows that we want
    df_all= df[df['c_resid,unit,nace_r2,geo\\time'].str.contains("FOR,NR,I551-I553,EL|FOR,NR,I551-I553,ES",regex=True)]#filtering.Keep only the columns and rows tha we want
    df_all= df_all[['2016 ', '2017 ', '2018 ', '2019 ']]

    print(df_all)
    return df_all
#execute function
df_night_NON= download_file(url, 'Night1.gz', 'Night2_NON.txt')
df_arrivals_NON= download_file(url1, 'Arrivals1.gz', 'Arrivals2_NON.txt')

def download_file1(url, file1, file2):
    r = requests.get(url, allow_redirects=True)
    open(file1, 'wb').write(r.content)
    with gzip.open(file1, 'rb') as f_in:      #Decompress gzip File
        with open(file2, 'wb') as f_out:      #convert gz in txt
            shutil.copyfileobj(f_in, f_out)

    df = pd.read_csv(file2, sep='\t', header=0)      #read the file as csv keeps only the columns and rows that we want
    df_all= df[df['c_resid,unit,nace_r2,geo\\time'].str.contains("TOTAL,NR,I551-I553,EL|TOTAL,NR,I551-I553,ES",regex=True)]#filtering.Keep only the columns and rows tha we want
    df_all = df_all[['2016 ', '2017 ', '2018 ', '2019 ']]

    print(df_all)
    return df_all

#execute function
df_night= download_file1(url, 'Night1.gz', 'Night2.txt')
df_arrivals= download_file1(url1, 'Arrivals1.gz', 'Arrivals2.txt')


#ploting
print(df_night_NON.T)#changes columns to rows and rows to columns
df_night_NON_T = df_night_NON.T
df_night_NON_T["Year"] = df_night_NON.keys()#contains the 4 years  of the dictionary as a list
print(df_night_NON_T)
df_night_NON_T=df_night_NON_T.rename(columns= {10: 'greece',11: 'Spain'}, inplace = False) #changes the name of the  columns
print(df_night_NON_T)
df_night_NON_T= df_night_NON_T.reset_index()
print(df_night_NON_T)
df_night_NON_T = df_night_NON_T.drop(columns="index")#avoid the old index
#sql : insert the values of dataframe into table
sql = "INSERT INTO `NIGHT_NON` (`year`, `greece`, `spain`) VALUES (%s, %s, %s)"
for i,row in df_night_NON_T.iterrows():
    cursor.execute(sql, (row["Year"], row["greece"], row["Spain"]))
    print(row)
db.commit()
#To verify the results print the values of table
for i,row in df_night_NON_T.iterrows():
    cursor.execute("SELECT * FROM  NIGHT_NON")
    print(cursor.fetchall())
#bar ploting  data of link
df_night_NON_T = df_night_NON_T.astype(float)
ax = plt.gca()
df_night_NON_T.plot(kind='bar', y=['greece','Spain'],x='Year',ax=ax)
plt.title('Nights spent at tourist accommodation establishments by non-residents')
plt.show()




print(df_arrivals_NON.T)
df_arrivals_NON_T = df_arrivals_NON.T
df_arrivals_NON_T["Year"] = df_arrivals_NON.keys()
print(df_arrivals_NON_T)
df_arrivals_NON_T=df_arrivals_NON_T.rename(columns= {10: 'greece',11: 'Spain'}, inplace = False)
df_arrivals_NON_T = df_arrivals_NON_T.reset_index()
print(df_arrivals_NON_T)
df_arrivals_NON_T = df_arrivals_NON_T.drop(columns="index")
print(df_arrivals_NON_T)
#sql : insert the values of dataframe into table
sql = "INSERT INTO `ARRIVALS_NON` (`year`, `greece`, `spain`) VALUES (%s, %s, %s)"
for i,row in df_arrivals_NON_T.iterrows():
   cursor.execute(sql, (row["Year"], row["greece"], row["Spain"]))
   print(row)
db.commit()
#To verify the results print the values of table
for i,row in df_arrivals_NON_T.iterrows():
    cursor.execute("SELECT * FROM ARRIVALS_NON ")
    print(cursor.fetchall())
df_arrivals_T = df_arrivals_NON_T.astype(float)
#bar ploting  data of link
ax = plt.gca()
df_arrivals_T.plot(kind='bar', y=['greece','Spain'],x='Year',ax=ax)
plt.title('Arrivals of non-residents at tourist accommodation establishments')
plt.show()

print(db)

#ploting
print(df_night.T)#changes columns to rows and rows to columns
df_night_T = df_night.T
df_night_T["Year"] = df_night.keys()#contains the 4 years  of the dictionary as a list
print(df_night_T)
df_night_T=df_night_T.rename(columns= {90: 'greece',91: 'Spain'}, inplace = False) #changes the name of the  columns
print(df_night_T)
df_night_T = df_night_T.reset_index()
print(df_night_T)
df_night_T = df_night_T.drop(columns="index")#avoid the old index
#sql : insert the values of dataframe into table
sql = "INSERT INTO `NIGHT` (`year`, `greece`, `spain`) VALUES (%s, %s, %s)"
for i,row in df_night_T.iterrows():
    cursor.execute(sql, (row["Year"], row["greece"], row["Spain"]))
    print(row)
db.commit()
#To verify the results print the values of table
for i,row in df_night_T.iterrows():
    cursor.execute("SELECT * FROM  NIGHT")
    print(cursor.fetchall())
#bar ploting  data of link
df_night_T = df_night_T.astype(float)
ax = plt.gca()
df_night_T.plot(kind='bar', y=['greece','Spain'],x='Year',ax=ax)
plt.title('Nights spent at tourist accommodation establishments ')
plt.show()

print(df_arrivals.T)
df_arrivals_T = df_arrivals.T
df_arrivals_T["Year"] = df_arrivals.keys()
print(df_arrivals_T)
df_arrivals_T=df_arrivals_T.rename(columns= {90: 'greece',91: 'Spain'}, inplace = False)
df_arrivals_T = df_arrivals_T.reset_index()
print(df_arrivals_T)
df_arrivals_T = df_arrivals_T.drop(columns="index")
print(df_arrivals_T)
#sql : insert the values of dataframe into table
sql = "INSERT INTO `ARRIVALS` (`year`, `greece`, `spain`) VALUES (%s, %s, %s)"
for i,row in df_arrivals_T.iterrows():
   cursor.execute(sql, (row["Year"], row["greece"], row["Spain"]))
   print(row)
db.commit()
#To verify the results print the values of table
for i,row in df_arrivals_T.iterrows():
    cursor.execute("SELECT * FROM ARRIVALS ")
    print(cursor.fetchall())
df_arrivals_T = df_arrivals_T.astype(float)
#bar ploting  data of link
ax = plt.gca()
df_arrivals_T.plot(kind='bar', y=['greece','Spain'],x='Year',ax=ax)
plt.title('Arrivals  at tourist accommodation establishments')
plt.show()


#converting all the dataframes in csv files
df_night_NON.to_csv('nights_non.csv',index=False)

df_arrivals_NON.to_csv('arrivals_non.csv',index=False)

df_night.to_csv('nights_total.csv',index=False)

df_arrivals.to_csv('arrivals_total.csv',index=False)
#verification of results
df_final_nights_non = pd.read_csv('nights_non.csv', sep=',', header=0)

df_final_arrivals_non = pd.read_csv('arrivals_non.csv', sep=',', header=0)

df_final_nights_total = pd.read_csv('nights_total.csv', sep=',', header=0)

df_final_arrivals_total = pd.read_csv('arrivals_total.csv', sep=',', header=0)
#print
df_final_nights_non = pd.read_csv('nights_non.csv', sep=',', header=0)
print(df_final_nights_non)

df_final_arrivals_non = pd.read_csv('arrivals_non.csv', sep=',', header=0)
print(df_final_arrivals_non)

df_final_nights_total = pd.read_csv('nights_total.csv', sep=',', header=0)
print(df_final_nights_total)

df_final_arrivals_total = pd.read_csv('arrivals_total.csv', sep=',', header=0)
print(df_final_arrivals_total)


