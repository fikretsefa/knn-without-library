**Kütüphane kullanmadan knn ile cihaz tüketim verileri tahmini**

<img src="https://media.giphy.com/media/kGkrWys2NoYGqqqlzW/giphy.gif" width="280" >

Kütüphane kullanmadan en yakın komşu algoritması oluşturulmaya çalışılmıştır.
En yakın komşu algoritması en kolay algoritmalardan biri olmasına rağmen yüksek doğruluk oluşturabilmektedir.
Veri seti ile karşılaştırılan verinin mevcut verilere olan uzaklığı hesaplanarak k sayıda yakın komşuluğuna bakılır.
Matematikte birçok uzaklık fonksiyonu kullanılmaktadır. 
Ancak knn’de Öklid, Manhattan ve Minkowski kullanılmaktadır. (Hamming,Consine)
Projede öklid uzaklığını kullandık.
En yakın komşu en yakın etiket demektir.

**Kod Hakkında**
<br>
Genel olarak test verileri içerisinden rastgele değişken seçilir. 
Bu değişken girdiğimiz k faktörüne göre eğitim verisindeki veriler ile Öklid uzaklığını hesaplar ve en kısa mesafeyi alır.
Eğer komşu sayısı 1’den büyük ise en kısa mesafeyi diziden çıkararak tekrar en kısa mesafe bulmaya çalışır.
Ve en kısa mesafe dizisinden bulunan değerlerden en çok bulunan tespit edilir.

<a target="_blank" href="https://github.com/fikretsefa/knn-without-library/edit/main/diagram.png" >Diagram</a>

**Kaynak**
<br>
<a target="_blank" href="https://github.com/CihanBosnali/Machine-Learning-without-Libraries" >Yardımcı Kaynak</a>

