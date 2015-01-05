python_mySQL
============

Pull data from a Table stored in a [MySQL database](http://mysql.com/products/workbench/) into a [pandas](http://pandas.pydata.org/) dataframe object within the [IPython](http://ipython.org/) environment. 


#### How To:

1. Install the following dependencies (python modules), which are packaged together in the [Enthought Python Distribtuion](https://www.enthought.com/products/canopy/): `pandas`, `pymysql`, `sys`, `numpy`, `datetime`, `os`.
 

2. Specify details about the MySQL Database, the Schema and Datatable you wish to connect with, and a local directory you wish to save a local copy to:

#####Example: 

MySQL instance = `localhost: 3306`, `user = root`, `passwd = ' '` 

Schema = `SXT_datamatrix`, Table = `Mouse_Cells_ALL`

Local directory to save Dataframe: `cd /Users/elizabethasmith/Desktop/sql`

Screenshot of IPython Notebook:

![Screenshot of IPython Notebook](https://github.com/elizabethizzysmith/python_mySQL/blob/master/ScreenShot.png)



**Licensed under the [MIT license](http://www.opensource.org/licenses/mit-license.php) -- see 'license.txt'

