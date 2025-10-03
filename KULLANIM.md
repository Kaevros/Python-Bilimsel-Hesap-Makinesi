# Bilimsel Hesap Makinesi - Kullanım Kılavuzu

## Buton Düzeni

Hesap makinesinin buton düzeni aşağıdaki gibidir:

```
┌──────────────────────────────────────────────┐
│        [ D İ G İ T A L   E K R A N ]         │
│               (Yeşil LED Ekran)               │
└──────────────────────────────────────────────┘

┌─────┬─────┬─────┬─────┬─────┐
│ sin │ cos │ tan │ log │  C  │  ← Bilimsel Fonksiyonlar & Temizle
├─────┼─────┼─────┼─────┼─────┤
│  √  │ x²  │ xʸ  │  (  │  )  │  ← Üslü İşlemler & Parantez
├─────┼─────┼─────┼─────┼─────┤
│  7  │  8  │  9  │  /  │  ←  │  ← Sayılar & Bölme & Geri
├─────┼─────┼─────┼─────┼─────┤
│  4  │  5  │  6  │  *  │  π  │  ← Sayılar & Çarpma & Pi
├─────┼─────┼─────┼─────┼─────┤
│  1  │  2  │  3  │  -  │  e  │  ← Sayılar & Çıkarma & Euler
├─────┼─────┼─────┼─────┼─────┤
│  0  │  .  │  =  │  +  │ ANS │  ← Sıfır & Ondalık & Eşittir & Toplama & Cevap
└─────┴─────┴─────┴─────┴─────┘
```

## Buton Açıklamaları

### Sayı Butonları (Gri)
- **0-9**: Rakamları girmek için
- **.**: Ondalık nokta

### Operatör Butonları (Turuncu)
- **+**: Toplama
- **-**: Çıkarma
- **×**: Çarpma
- **÷**: Bölme
- **=**: Hesapla

### Bilimsel Fonksiyon Butonları (Koyu Gri)
- **sin**: Sinüs (derece cinsinden)
- **cos**: Kosinüs (derece cinsinden)
- **tan**: Tanjant (derece cinsinden)
- **log**: 10 tabanında logaritma
- **√**: Karekök
- **x²**: Karesi
- **xʸ**: x üzeri y

### Özel Butonlar
- **C**: Ekranı temizle (açık gri)
- **←**: Son karakteri sil (açık gri)
- **(**: Sol parantez
- **)**: Sağ parantez
- **π**: Pi sayısı (3.14159...)
- **e**: Euler sayısı (2.71828...)
- **ANS**: Son hesaplama sonucu

## Kullanım Örnekleri

### 1. Basit Aritmetik
**Soru:** 25 + 37 = ?

**Adımlar:**
1. `2` → `5` tıkla
2. `+` tıkla
3. `3` → `7` tıkla
4. `=` tıkla

**Sonuç:** 62

---

### 2. Trigonometrik İşlem
**Soru:** sin(30°) = ?

**Adımlar:**
1. `3` → `0` tıkla
2. `sin` tıkla

**Sonuç:** 0.5

---

### 3. Karekök
**Soru:** √144 = ?

**Adımlar:**
1. `1` → `4` → `4` tıkla
2. `√` tıkla

**Sonuç:** 12

---

### 4. Üslü Sayı
**Soru:** 5³ = ?

**Adımlar:**
1. `5` tıkla
2. `xʸ` tıkla
3. `3` tıkla
4. `=` tıkla

**Sonuç:** 125

---

### 5. Logaritma
**Soru:** log₁₀(1000) = ?

**Adımlar:**
1. `1` → `0` → `0` → `0` tıkla
2. `log` tıkla

**Sonuç:** 3

---

### 6. Parantezli İşlem
**Soru:** (15 + 5) × 3 = ?

**Adımlar:**
1. `(` tıkla
2. `1` → `5` tıkla
3. `+` tıkla
4. `5` tıkla
5. `)` tıkla
6. `*` tıkla
7. `3` tıkla
8. `=` tıkla

**Sonuç:** 60

---

### 7. Pi ile İşlem
**Soru:** 2πr (r=5) = ?

**Adımlar:**
1. `2` tıkla
2. `*` tıkla
3. `π` tıkla
4. `*` tıkla
5. `5` tıkla
6. `=` tıkla

**Sonuç:** 31.41592... (çemberin çevresi)

---

### 8. Karmaşık İşlem
**Soru:** √(25) + 3² = ?

**Adımlar:**
1. `2` → `5` tıkla
2. `√` tıkla (sonuç: 5)
3. `+` tıkla
4. `3` tıkla
5. `x²` tıkla (sonuç: 9)
6. `=` tıkla

**Sonuç:** 14

---

## İpuçları

1. **Hatalı Giriş:** Eğer yanlış bir şey girerseniz, `←` tuşu ile son karakteri silebilir veya `C` ile tümünü temizleyebilirsiniz.

2. **Son Sonuç:** `ANS` butonu, son hesaplama sonucunu getirir. Bu özellikle zincir hesaplamalarda kullanışlıdır.

3. **Trigonometrik Fonksiyonlar:** Sin, cos ve tan fonksiyonları **derece** cinsinden çalışır. Örneğin, sin(90) = 1 sonucunu verir.

4. **Ondalık Sayılar:** Ondalık sayıları girmek için `.` butonunu kullanın. Örnek: 3.14

5. **Negatif Sayılar:** Negatif sayı girmek için, `0` → `-` → sayı şeklinde girebilirsiniz.

## Hata Mesajları

Uygulama aşağıdaki durumlarda hata mesajı gösterir:

- **"Sıfıra bölme hatası"**: Bir sayıyı 0'a bölmeye çalıştığınızda
- **"Negatif sayının karekökü alınamaz"**: Negatif bir sayının karekökünü almaya çalıştığınızda
- **"Log sadece pozitif sayılar için"**: Sıfır veya negatif sayının logaritmasını almaya çalıştığınızda
- **"Geçersiz ifade"**: Matematiksel olarak geçersiz bir ifade girdiğinizde
- **"Geçersiz sayı"**: Sayı formatı yanlış olduğunda

## Klavye Kısayolları

Şu an için uygulama sadece fare ile çalışmaktadır. Gelecek sürümlerde klavye desteği eklenebilir.

## Sık Sorulan Sorular

**S: Trigonometrik fonksiyonlar radyan mı derece mi kullanıyor?**
C: Derece kullanıyor. sin(90) = 1 sonucunu verir.

**S: Kaç haneli hassasiyet var?**
C: Python'un math kütüphanesinin sağladığı tam hassasiyet (genellikle 15-17 anlamlı basamak).

**S: Negatif sayı nasıl girilir?**
C: 0 - sayı şeklinde girebilirsiniz. Örneğin -5 için: 0 - 5

**S: Bilimsel notasyon destekleniyor mu?**
C: Şu an desteklenmemektedir, ancak çok büyük veya küçük sayılar otomatik olarak bilimsel notasyonda gösterilir.

**S: Hafıza fonksiyonu var mı?**
C: ANS butonu son sonucu saklar. Daha gelişmiş hafıza fonksiyonları şu an bulunmamaktadır.

## Güncelleme Notları

### Versiyon 1.0
- İlk sürüm
- Temel aritmetik işlemler
- Trigonometrik fonksiyonlar (sin, cos, tan)
- Logaritma ve karekök
- Üslü sayı hesaplama
- Parantez desteği
- Pi ve Euler sabitleri
- Hata yönetimi
