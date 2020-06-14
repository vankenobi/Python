isim LIKE 'Ko%' # isim kolonunda başı KO ile başlayan isimi arar.
# bunun yerine CTRL+F kombinasyonunu da kullanabilirsin.
SELECT isim FROM gorevliler; #Görev görevliler listesindeki isim sütununu gösterir.
#-----------
SELECT isim
FROM
     (SELECT *
      FROM gorevliler
      WHERE numara = '4J48'
     )
#Numarası 4j48 olan kişiyi göster
SELECT 
	isim
FROM
    SELECT *
     	FROM gorevliler
        WHERE yaş BETWEEN :alt AND : ust
        
#Parametreli sorgu yapmak için kullanılır.
SELECT
    isim
FROM gorevliler
WHERE yaş < 40;
#Yaşı 40 dan küçük kişilerin isim bilgisini getir.
SELECT
    isim,
    soyisim
FROM gorevliler
WHERE isim LIKE 'Mus%' 
#Adı Mus ile başlayan isimleri ekrana getir. Yani baştan arama yapar. 'Musa%'
SELECT
    isim,
    soyisim
FROM gorevliler
WHERE isim LIKE '%n'
# İsminin son harfi n olan kişileri getirir yani sondan arama yapar ''
SELECT
    isim,
    soyisim
FROM gorevliler
WHERE isim LIKE '_e%'
#isminin ikinci harfi e ile başlayan kişileri verir. Her '_' işareti boşa geçen bir karakteri temsil eder.
SELECT
    isim,
    soyisim
FROM gorevliler
WHERE isim LIKE  '%sa'
#isimin ilk kısmını bilmiyorum ama  şöyle devam ediyor.
SELECT
    isim,
    soyisim
FROM gorevliler
WHERE isim LIKE  'M__a'
# Farklı bir arama şekli 
