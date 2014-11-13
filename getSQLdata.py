#!/usr/bin/python

# %run getSQLdata.py SXT_datamatrix Mouse_Cells_ALL

import pymysql
import sys
import numpy as np
import pandas as pd
import time
import datetime
import os

#define a function getSQL data, which pulls all data from specified database and data table into a list of equal-length lists

dir = '/Users/elizabethasmith/Desktop/sql'
os.chdir(dir)

myList = []

def main():
    
    print 'Retrieving data from the ' + sys.argv[2] + ' table from the ' + sys.argv[1] + ' My SQL database...\n ' 
  
    #generate a reference to the database, stored as connection. Database specified by arguments 
    
    connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db= sys.argv[1])

    
    cursor = connection.cursor()

    myquery = 'SELECT * FROM ' + sys.argv[1] + '.' + sys.argv[2]
    
    #cursor.execute(myquery)
    #allRows = cursor.fetchall()

    cursor.execute(myquery)
    
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    
    for row in cursor: 
        rowList = []
        for item in row:
            rowList.append(item)
        myList.append(rowList)     
    
    dataset = np.array(myList)
    
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
    
    datasetname = sys.argv[1]+ '_' + sys.argv[2]+'_'+ st    
    
    global df
    
    df = pd.DataFrame(myList, columns = field_names)
    
    df.to_pickle(datasetname)  
    
    #print dataset.shape[0]   
    #print num_fields
    
    if myList == []:
        print 'I did not find any data there.  Are you sure you have the correct name?'
    
    else:    
        print 'Success!  You just pulled out ' + str(dataset.shape[0]) + ' rows, each of which contained ' + str(dataset.shape[1]) + ' columns, of data.\n' 
        print 'You also pulled out ' + str(num_fields) + ' field names.\n'
        print 'These data have been saved in a pandas Dataframe called ' + datasetname + '.npy locally at '+ dir +'.\n'
        print 'The Dataframe is also present as a global variable called "df".\n'


    cursor.close()
    connection.close()

     
#boilerplate to call the function and begin the program.
     
if __name__ == '__main__':
  main()
