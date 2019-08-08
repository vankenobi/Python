/*
  ORDER BY İLE SIRALAMA İŞLEMİ 
 */

SELECT * FROM gorevliler
ORDER BY yaş 
 # görevliler listesini yaşa göre sıralamak 
SELECT * FROM gorevliler
ORDER BY  yaş DESC   Descending 
#yaşları azalan bir sıraya göre dizmek = azalan
SELECT * FROM gorevliler
ORDER BY  yaş ASC
# Yaşları artan bir sıraya göre dizmek ascending = yükselen
SELECT 10/5 AS RESULT;
SELECT 2+3;
# Aritmetik işlemler
SELECT 'CİHAN ' || 'TAVUK' AS Full_Name
#Veya
SELECT 'CİHAN' || ' ' || 'TAVUK' AS Full_Name
# Metinsel birleştirme operatörü 
###############################
SELECT concat('İsim',' ','Soyisim') #örnek bir sütun oluşturup içerisine isim ve soyisim yazdı. 
SELECT concat(isim, ' ',soyisim) AS Full_Name
FROM gorevliler

SELECT concat('veri girişi',NULL) AS İsimler;
###############################################
SELECT concat('sayimiz',5) AS DATA; # string bir ifade ile int bir ifadeyi birleştirdiğimiz için AS DATA yazdık.
###############################################
SELECT isim, 
       concat('ADINIZ:',length(isim),' karakter içeriyor') # length fonksiyonu ile isim kelimesinin kaç karakter içerdiğini buluyoruz.
FROM gorevliler
