# Python-Bilimsel-Hesap-Makinesi

Bu proje, Python'un standart Tkinter kütüphanesiyle sıfırdan geliştirilmiş, basit ve güçlü bir bilimsel hesap makinesidir. Amacım, hem günlük dört işlemi hem de sinüs, kosinüs, logaritma ve üslü sayılar gibi bilimsel fonksiyonları kolayca yapabilen, temiz bir ara yüze sahip, hafif bir masaüstü uygulaması oluşturmaktı.

## Özellikler

### Temel Aritmetik İşlemler
- ✓ Toplama (+)
- ✓ Çıkarma (-)
- ✓ Çarpma (*)
- ✓ Bölme (/)

### Bilimsel Fonksiyonlar
- ✓ **sin** - Sinüs (derece cinsinden)
- ✓ **cos** - Kosinüs (derece cinsinden)
- ✓ **tan** - Tanjant (derece cinsinden)
- ✓ **log** - Logaritma (10 tabanında)
- ✓ **√** - Karekök
- ✓ **x²** - Kare
- ✓ **xʸ** - Üslü sayı hesaplama

### Ek Özellikler
- ✓ **π** - Pi sayısı (3.14159...)
- ✓ **e** - Euler sayısı (2.71828...)
- ✓ **ANS** - Son hesaplama sonucu
- ✓ **()** - Parantez desteği
- ✓ **C** - Temizle
- ✓ **←** - Geri al (backspace)

### Kullanıcı Arayüzü
- Geniş ve okunabilir ekran
- Koyu tema ile modern görünüm
- Renkli ve düzenli butonlar
- Hata mesajları ile kullanıcı dostu arayüz

## Gereksinimler

- Python 3.6 veya üzeri
- Tkinter (çoğu Python kurulumunda varsayılan olarak gelir)

### Tkinter Kurulumu (Gerekirse)

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**macOS ve Windows:**
Varsayılan Python kurulumunda Tkinter zaten mevcuttur.

## Kurulum ve Çalıştırma

1. Projeyi klonlayın:
```bash
git clone https://github.com/Kaevros/Python-Bilimsel-Hesap-Makinesi.git
cd Python-Bilimsel-Hesap-Makinesi
```

2. Uygulamayı çalıştırın:
```bash
python3 hesap_makinesi.py
```

## Kullanım

### Temel İşlemler
1. Sayıları ve operatörleri sırayla tıklayın
2. **=** tuşuna basarak sonucu görün
3. **C** ile ekranı temizleyin
4. **←** ile son karakteri silin

### Bilimsel Fonksiyonlar
1. Bir sayı girin
2. İlgili fonksiyon butonuna tıklayın (sin, cos, tan, log, √, x²)
3. Sonuç otomatik olarak hesaplanır

### Üslü Sayı Hesaplama
1. Taban sayıyı girin
2. **xʸ** butonuna tıklayın
3. Üs değerini girin
4. **=** ile hesaplayın

### Örnekler

**Örnek 1: Basit Toplama**
```
5 + 3 = 8
```

**Örnek 2: Trigonometrik İşlem**
```
sin(30) = 0.5
```

**Örnek 3: Karekök**
```
√16 = 4
```

**Örnek 4: Üslü Sayı**
```
2 xʸ 8 = 256
```

**Örnek 5: Parantezli İşlem**
```
(5 + 3) * 2 = 16
```

## Test

Matematiksel fonksiyonların doğruluğunu test etmek için:

```bash
python3 test_hesap_makinesi.py
```

Test paketi şunları içerir:
- Temel aritmetik işlemler
- Bilimsel fonksiyonlar
- Özel değerler (π, e)
- Hata yönetimi
- Karmaşık ifadeler

## Teknik Detaylar

### Kullanılan Kütüphaneler
- **tkinter** - Grafik kullanıcı arayüzü
- **math** - Matematiksel hesaplamalar

### Özellikler
- Temiz ve modüler kod yapısı
- Kapsamlı hata yönetimi
- Sıfıra bölme koruması
- Negatif sayıların karekökü kontrolü
- Geçersiz logaritma kontrolü
- Kullanıcı dostu hata mesajları

### Hata Yönetimi
Uygulama aşağıdaki hatalara karşı korumalıdır:
- Sıfıra bölme
- Negatif sayıların karekökü
- Negatif veya sıfır değerli logaritma
- Geçersiz matematiksel ifadeler
- Geçersiz sayı formatları

## Ekran Görüntüleri

Uygulama modern, koyu temalı bir arayüze sahiptir:
- Yeşil renkli dijital ekran
- Turuncu renkte operatör butonları
- Gri tonlarda rakam ve fonksiyon butonları
- 400x600 piksel pencere boyutu

## Geliştirici

Bu proje, Python ve Tkinter kullanılarak sıfırdan geliştirilmiştir. Kod temiz, okunabilir ve kolayca genişletilebilir yapıdadır.

## Lisans

Bu proje açık kaynak kodludur ve eğitim amaçlı kullanılabilir.

## Katkıda Bulunma

Önerileriniz ve katkılarınız için pull request gönderebilirsiniz.
