  import sqlite3
db = sqlite3.connect("book.sqlite")
imlec = db.cursor()
"""
Yeni bir tablo açmak için kullanılır parantez içerisine 
yazılanlar sütun bilgilerini verir.
"""
imlec.execute("CREATE TABLE IF NOT EXISTS kitaplistesi (yazar,kitap)") 
"""
eklenecek tabloyu ve kitap + yazar parametrelerini alır.
"""
imlec.execute("INSERT INTO 'kitaplistesi' VALUES ('YAŞAR KEMAL','FIRAT SUYU KAN AKIYOR BAKSANA')")
imlec.execute("CREATE TABLE IF NOT EXISTS 'kitapkayitx' (yazar,kitap)")
imlec.execute("INSERT INTO 'kitapkayitx' VALUES ('TARIK BUĞRA','Küçük Ağa')")
imlec.execute("INSERT INTO 'kitaplistesi' VALUES ('JOSE MAURO ','ŞEKER PORTAKALI')")
db.commit()
db.close()
