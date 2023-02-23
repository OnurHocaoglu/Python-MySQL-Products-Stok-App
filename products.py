from connection import connection
import mysql.connector


class Products:

    def insertProduct(self,list):

        mycursor = connection.cursor()

        sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"

        values = list

        mycursor.executemany(sql,values) # sql verilerini gönderdik 


        try:
            connection.commit() # veriler databaseye commitlendi
            print(f"{mycursor.rowcount} tane kayıt eklendi") 
            print(f"son eklenen kaydın id: {mycursor.lastrowid}") # son eklenen id
        except mysql.connector.Error as error:
            print("hata:",error)
        finally:
            print("Database bağlantısı kapatıldı!!")

    def getProducts(self):

        mycursor = connection.cursor()

        mycursor.execute("Select * From Products")

        try:
            resultt = mycursor.fetchall()
            for result in resultt:
                print(f"id : {result[0]} name: {result[1]} Fiyat: {result[2]} İmageUrl: {result[3]} Açıklama: {result[4]}")
        except mysql.connector.Error as err:
            print("hata", err)


    def searchProducts(self,name):

        mycursor = connection.cursor()

        mycursor.execute(f"Select * From Products Where name LIKE '%{name}%'")

        try:
            resultt = mycursor.fetchall()
            for result in resultt:
                print(f"id : {result[0]} name: {result[1]} Fiyat: {result[2]}")
        except mysql.connector.Error as err:
            print("hata", err)

    def updateProducts(self,change_id,new_name,new_price,new_image,new_description):

        mycursor = connection.cursor()

        mycursor.execute(f"Update products Set name='{new_name}',price={new_price},imageUrl='{new_image}',description='{new_description}' where id='{change_id}'")

        try:
            connection.commit() 
            print(f"{mycursor.rowcount} tane kayıt güncellenmiştir.")
        except mysql.connector.Error as error:
            print("hata:",error)


    def deleteProducts(self,id):

        mycursor = connection.cursor()

        mycursor.execute(f"delete from products where id={id}")

        try:
            connection.commit()
            print(f"{mycursor.rowcount} tane kayıt silinmiştir.")
        except mysql.connector.Error as error:
            print("hata:",error)