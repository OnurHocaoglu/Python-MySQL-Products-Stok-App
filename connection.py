import mysql.connector
# MySQL Local instance

# Table Products , Columns id,name,price,imageUrl,description,categoryid

# Table Categories , Colums  id,name

connection = mysql.connector.connect(host = "localhost",
    user = "root", # user
    password = "yourpass", # password
    database = "node-app",
    ) 