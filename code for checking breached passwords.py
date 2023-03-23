import mysql.connector

# connect to the MySQL database
connector= mysql.connector.connect(user='sanga123', 
password='breached6789!!', host='breachedpasswords.mysql.database.azure.com',
 port=3306, database='breachedpasswords')

# get password from the user
passwordinput = input("Enter password:")

# define the query
query = "SELECT * FROM passwords WHERE Password = %s"

# execute the query with the user entered password as a parameter
cursor = connector.cursor()
cursor.execute(query, (passwordinput,))

# check if any passwords were returned
result = cursor.fetchone()
if result:
  print("Password entered is a breached password.")
else:
    print("Password entered is not a breached password")
connector.close()
