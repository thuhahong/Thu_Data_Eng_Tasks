import sqlalchemy
import pyodbc
import pandas as pd

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'SQL Server'
engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")
# create engine(dialect, driver, user, password, etc)

connection = engine.connect()
# creating a connection to sql - so that we can select and manipulate data from tables etc

results = engine.execute('SELECT * FROM Products;')
print(results.fetchall())

# execute queries
# results = engine.execute('SELECT * FROM products;') # this will return an object we will need to access
# print(f"\n{results}")
#
# returning the headers of results (which in this case, is the products table)
# headers = results.keys()
# print(headers)
#
# retrieve one row at a time from your result
# first_row = results.fetchone()
# print(first_row)
#
# retrieve multiple rows at a time
# many_rows = results.fetchmany(10) # here we will need to specify how many we want to retrieve
# print(many_rows)
#
# retrieving everything
# all_results = results.fetchall()
# print(all_results)
#
# Note: Printing results like this causes some interesting effects
# E.g. When you print many_rows, it returns Rows 2-11, rather than 1-10
# And then when you print all, it prints from Row 12, rather than Row 1
#
# print("\n")
#
# When getting a string from the SQL table via a WHERE clause, you MUST use single quotes!
# Otherwise, you get an error saying, to an extent, "... is an invalid column"
# That means that, in general, it's probably a good idea to use double quotes when running queries!
#
# chai = engine.execute("SELECT * FROM products WHERE ProductName = 'Chai';")
#
# Even then, you still need to fetch the results, chai is still just an object!
# print(chai)
# print(chai.fetchall())
#
# Discontinued Products
# discontinued = engine.execute("SELECT ProductName FROM products WHERE Discontinued = 'True';")
# print(discontinued)
# print(discontinued.fetchone())
# print(discontinued.fetchall())
#
# Joining onto Categories table
# join_categoryID = engine.execute("SELECT * FROM Products p\n JOIN Categories c ON p.CategoryID = c.CategoryID;")
# print("\n")
# print(join_categoryID.keys())

# Iterating through and printing first 5 items in the joined table
# for item in join_categoryID.fetchmany(5):
# print(item)

# Creating a pandas DataFrame!
# products_df = pd.read_sql_query(query, engine)
# print(products_df)
# print(products_df.describe())

# pandas

# query = 'SELECT * FROM Products;'
# products_df = pd.read_sql_query(query, engine) #using method to pass in query and then the connection

# this is now a dataframe, meaning we can interact with the data with pandas and numpy easily
#
# print(products_df.describe())
