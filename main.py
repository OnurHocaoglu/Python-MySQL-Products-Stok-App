from products import Products

products = Products() 

# onurhocaoglu.com Coded By OnurHocaoglu

# MySQL Local instance

# Menu 
while True:
    print("----------------Ürün Stok App----------------")

    print("1-Ürün Ekle\n2-Ürün Listeleme\n3-Ürün Arama\n4-Güncelleme\n5-Ürün Silme\n6-Çıkış")

    enter = input("Seçim Yapınız: ")

    if enter == "1":

        liste =[]

        while True:

            name = input("Ürün Adı : ")

            price = float(input("Fiyat : "))

            imageUrl = input("Ürün Resim Adı : ")

            description = input("Ürün Açıklaması : ")

            liste.append((name,price,imageUrl,description))

            enter = input("Devam etmek istiyor musunuz ? (e/h)")

            if enter == "h":
                
                print("Kayıtlar Eklendi.")

                print(liste)

                products.insertProduct(liste)

                break

            elif enter == "e":

                continue

            else:
                print("Yanlış değer girildi")

                break

    elif enter == "2":

        products.getProducts()

    elif enter == "3":

        search = input("Aranacak Ürünü Giriniz: ")

        products.searchProducts(search)

    elif enter == "4":

        products.getProducts() # Listeleme (Güncelleme)

        change_id = input("Değişecek ürün ID giriniz: ")

        change_name = input("Ürünün yeni adını giriniz : ")

        change_price = input("Ürünün yeni fiyatını giriniz : ")

        change_image = input("Ürünün yeni fotografını giriniz : ")

        change_description = input("Ürünün yeni açıklamasını giriniz : ")

        products.updateProducts(change_id,change_name,change_price,change_image,change_description)

    elif enter == "5":

        products.getProducts() # Listeleme (Ürün seçip silme işlemi)

        delete_id = input("Silinecek Ürünü ID'sini Giriniz: ")

        products.deleteProducts(delete_id)

    elif enter == "6":

        exit(0)

    else:

        print("Yanlış değer girildi !")


