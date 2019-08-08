CREATE TABLE companies
(
    ID INT,
    NAME CHAR,
    AGE INT,
    ADRESS varchar(50),
    PRICE REAL
);
#Tablo oluşturma

CREATE TABLE yeni_tablo AS (SELECT * FROM gorevliler) WITH NO DATA ;
SELECT * FROM yeni_tablo;
# gorevliler tablosunun sadece kalıbını aldık ve yeni tablo adlı yeni bir tablo oluşturduk.
CREATE TABLE yeni_tablo2 AS (SELECT * FROM gorevliler);
SELECT  * FROM yeni_tablo2;
#üsttekinden gorevliler tablosunun bire bir aynısını yenitablo2 isimli tablo oluşturup içerisine atması
CREATE TABLE kisiler
(
    ID SERIAL,
    isim varchar(50)
);
# id Serial ID üretir. ID sütununa 
SELECT currval(pg_get_serial_sequence('kisiler','id'))
# Serial ID'nin  en son nerede kaldığını gösterir. 
SELECT numara,isim,soyisim,boy
INTO TEMP TABLE ayrı
FROM gorevliler
WHERE boy < 1.78
ORDER BY isim;

SELECT * FROM ayrı;
# geçici tablo

ALTER TABLE tablo_ismi DROP sütun_ismi; # silmek istediğiniz sütunu siler.
#####################
ALTER TABLE MSA RENAME TO MSAC; #Tablo ismi değiştirmek için kullanır.
#####################
ALTER TABLE "msac" ADD COLUMN "yas" BIT(1); # yeni bir sütun eklemek için kullanılır.
#####################
DROP DATABASE IF EXISTS database_isim # database silmek için kullanılır.
DROP TABLE IF EXISTS tablo_isim #tablo silmek için kullanılır 
#####################
--Multiple INSERT 
INSERT INTO users(id, name) VALUES
(2,'Musa'),(3,'Mustafa'),(4,'SELİM');
##########UPDATE###############
UPDATE users
SET name = 'AHMET'
WHERE id = 4; # idsi 4 olan isimi Ahmet yaptık. 
#############
TRUNCATE TABLE table_name; # !!!!! (PEK FAZLA KULLANMA RİSKLİ)Tablonun içerisindeki bütün verileri siler
###############
CREATE TABLE IF NOT EXISTS Countries
(
  country_id SERIAL,
  country_name  varchar(40) CHECK ( country_name IN('Turkey','Germany','Italy'))
);
# ülke isim bilgisinde turkey germany ve italya dan başka isim olmuyacak.
ALTER TABLE kisiler ALTER COLUMN isim SET NOT NULL ;
# tablodaki isim sütununu doldurulması zorunlu hale getirdik.
CREATE TABLE  IF NOT EXISTS kisiler
(
    id SERIAL,
    isim VARCHAR(50) NOT NULL,
    soyisim VARCHAR(50) NOT NULL,
    tckimlik NUMERIC(11,0) NOT NULL,
    maas NUMERIC NOT NULL CHECK ( maas >=1600 )

);
# NOT NULL kesinlikle doldurulması gereken alan demek 
CREATE TABLE  IF NOT EXISTS kisiler
(
    id SERIAL,
    isim VARCHAR(50) NOT NULL,
    soyisim VARCHAR(50) NOT NULL,
    tckimlik NUMERIC(11,0) NOT NULL UNIQUE ,
    maas NUMERIC NOT NULL CHECK ( maas >=1600 )

);
# UNIQUE o sütunu benzersiz yapar yani (tc kimlik her kişi için farklıdır.)
	#Farklı bir kullanım şekli ise 
CREATE TABLE IF NOT EXISTS person
(
    id SERIAL,
    name VARChar(50) ,
    surname VARCHAR(62), 
    tc_no NUMERIC(11) ,
    UNIQUE (tc_no)
);
#########################
CREATE TABLE IF NOT EXISTS person
(
    id SERIAL,
    name VARChar(50) DEFAULT 'Name',
    surname VARCHAR(62) DEFAULT 'Surname' ,
    tc_no NUMERIC(11) ,
    UNIQUE (tc_no)
);

#DEFAUL eğer birşey girilmez ise sağındaki değerleri girecektir.
###############
CREATE TABLE IF NOT EXISTS otomobiller
(
    id SERIAL UNIQUE NOT NULL PRIMARY KEY ,
    marka varchar(55),
    model varchar(55),
    açıklama text,
    PRIMARY KEY (id)

);
 # otomobiller tablosundaki ID kısmını Primary Key yaptık.
 # Bir başka gösterim şekli 
CREATE TABLE IF NOT EXISTS otomobiller
(
    id SERIAL UNIQUE NOT NULL PRIMARY KEY ,
    marka varchar(55),
    model varchar(55),
    açıklama text,
    PRIMARY KEY (id)

);

###################
--PRIMERY KEY & FOREIGN KEY
 SELECT * FROM tablo_name
 WHERE sütun_name IN (değerler); # Girilen değerlerin var olduğu satırları gösterir.


 SELECT * FROM tablo_name
 WHERE sütun_name NOT IN (değerler); # Girilen değerlerin olmadığı satırları gösterir.

 SELECT LENGHT('Merhaba') # içerisine girilen yazının boyutunu verir.
 SELECT CHAR_LENGHT('Merhaba') # Aynı işlemi görür.
 SELECT LOWER('MERHABA'); #Büyük harfle yazılan metni küçük harfe çevirir.
 SELECT UPPER('merhaba'); #Küçük harfle yazılan metni büyük harfe çevirir.
 SELECT SUBSTR('Merhaba',2,4) # Çıktı: erh Kelimeyi kesmeye yarar.
 SELECT POSITION ('ha' in 'Merhaba') # Çıktı: 4 kelimenin neresinde olduğunu söylüyor.
 SELECT ASCII('a')  # Çıktı karakterin ASCII tablosundaki karşılığını verir.
 SELECT INITCAP('merhaba nasılsın'); # Çıktı: Merhaba Nasılsın Baş harfleri büyük çıkarır.
 SELECT REPEAT('hi',3); #çıktı hihihi ne kadar isterseniz yanyana yazar
 SELECT REVERSE('olleh') # Çıktı: hello  Terse çevirme işlemi yapar.
 SELECT count(*) FROM tablo_name #çıktı 50 Tabloda kaç satır olduğunu sayar.
 SELECT COUNT(DISTINCT yaş) FROM gorevliler; #üstteki ile aynı 
 SELECT MAX(yaş) FROM gorevliler; #tabloda belirtilen sütunda en yüksek değeri bulur.
 SELECT MIN(yaş) FROM gorevliler; #tabloda belirtilen sütundaki en düşük değeri bulur.
 SELECT SUM(yaş) AS toplamyaş FROM gorevliler;
 ##################

 SELECT SUM(ücret)
FROM hesaplar # grupluyor. idsi 1 olan kişi 3 tane 
GROUP BY id;

##############
SELECT SUM(ücret)
FROM hesaplar
GROUP BY id
HAVING SUM(ücret) > 200; # yukarıdakinin benzeri bir fark 200 ün üzerinde olanları gösterir.
##############
