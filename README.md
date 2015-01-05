python_mySQL
============

January 2015

If you are looking to pull data from a Table stored in a [MySQL database](http://mysql.com/products/workbench/) into a [pandas](http://pandas.pydata.org/) dataframe object within the [IPython](http://ipython.org/) environment, you might be interested in using this `getSQLdata.py` script & associated IPython notebook. 


#### How To:



1. Install the following dependencies (python modules), which are packaged together in the [Enthought Python Distribtuion](https://www.enthought.com/products/canopy/): `pandas`, `pymysql`, `sys`, `numpy`, `datetime`, `os`

2. Specify details about the MySQL Database and Data Table you wish to connect with:

Ex: MySQL instance = `localhost: 3306`, `user = root`, `passwd = ' '` 
    Table
