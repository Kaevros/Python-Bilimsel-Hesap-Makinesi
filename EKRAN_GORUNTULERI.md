# Ekran Görüntüleri ve Arayüz Tasarımı

## Ana Pencere

Hesap makinesi penceresi **400x600 piksel** boyutlarında, modern ve kullanıcı dostu bir arayüze sahiptir.

### Renk Paleti

```
Genel Tema: Koyu Tema (Dark Theme)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎨 Pencere Arkaplanı:    #2b2b2b (Koyu Gri)
📟 Dijital Ekran Zemin:  #1a1a1a (Çok Koyu Gri)
💚 Ekran Yazı Rengi:     #00ff00 (Neon Yeşil)
🔢 Sayı Butonları:       #404040 (Orta Gri)
➗ Operatör Butonları:   #ff9500 (Turuncu)
🔬 Fonksiyon Butonları:  #505050 (Gri)
⚪ Özel Butonlar:        #d4d4d2 (Açık Gri)
```

## Ekran Düzeni

```
┌────────────────────────────────────────┐
│  Bilimsel Hesap Makinesi          [X]  │
├────────────────────────────────────────┤
│                                        │
│  ┌──────────────────────────────────┐ │
│  │                                  │ │
│  │            0                     │ │ ← Dijital Ekran (Yeşil LED)
│  │                                  │ │   Font: Arial 24pt Bold
│  └──────────────────────────────────┘ │
│                                        │
│  ┌────┬────┬────┬────┬────┐          │
│  │sin │cos │tan │log │ C  │          │
│  ├────┼────┼────┼────┼────┤          │
│  │ √  │ x² │ xʸ │ (  │ )  │          │
│  ├────┼────┼────┼────┼────┤          │
│  │ 7  │ 8  │ 9  │ /  │ ←  │          │
│  ├────┼────┼────┼────┼────┤          │
│  │ 4  │ 5  │ 6  │ *  │ π  │          │
│  ├────┼────┼────┼────┼────┤          │
│  │ 1  │ 2  │ 3  │ -  │ e  │          │
│  ├────┼────┼────┼────┼────┤          │
│  │ 0  │ .  │ =  │ +  │ANS │          │
│  └────┴────┴────┴────┴────┘          │
│                                        │
└────────────────────────────────────────┘

Boyutlar: 400 x 600 piksel
Yeniden boyutlandırma: Kapalı
```

## Buton Özellikleri

### 1. Dijital Ekran
- **Font**: Arial, 24pt, Bold
- **Renk**: #00ff00 (Neon Yeşil LED efekti)
- **Arkaplan**: #1a1a1a (Siyah)
- **Hizalama**: Sağa dayalı
- **Özellikler**: 
  - Gömülü (Sunken) görünüm
  - 10px çerçeve kalınlığı
  - Yanıp sönen cursor (yeşil)

### 2. Sayı Butonları (0-9, .)
- **Boyut**: 5 karakter genişlik × 2 satır yükseklik
- **Font**: Arial, 14pt, Bold
- **Renk**: Beyaz yazı, #404040 arkaplan
- **Hover**: #505050 (Biraz daha açık gri)
- **Butonlar**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, .

### 3. Operatör Butonları (+, -, *, /, =)
- **Boyut**: 5 karakter genişlik × 2 satır yükseklik
- **Font**: Arial, 14pt, Bold
- **Renk**: Beyaz yazı, #ff9500 arkaplan (Turuncu)
- **Hover**: #ffad33 (Açık turuncu)
- **Butonlar**: +, -, *, /, =

### 4. Bilimsel Fonksiyon Butonları
- **Boyut**: 5 karakter genişlik × 2 satır yükseklik
- **Font**: Arial, 14pt, Bold
- **Renk**: Beyaz yazı, #505050 arkaplan
- **Hover**: #606060 (Biraz daha açık)
- **Butonlar**: sin, cos, tan, log, √, x², xʸ, (, ), π, e, ANS

### 5. Özel Butonlar (C, ←)
- **Boyut**: 5 karakter genişlik × 2 satır yükseklik
- **Font**: Arial, 14pt, Bold
- **Renk**: Siyah yazı, #d4d4d2 arkaplan (Açık gri)
- **Hover**: #e5e5e5 (Daha açık)
- **Butonlar**: C (Clear), ← (Backspace)

## Kullanım Senaryoları ve Ekran Görüntüleri

### Senaryo 1: Başlangıç Durumu
```
┌──────────────────────────────────┐
│              0                   │  ← İlk açılışta "0" görüntülenir
└──────────────────────────────────┘
```

### Senaryo 2: Basit Toplama (25 + 37)
```
Adım 1: "25" girildi
┌──────────────────────────────────┐
│             25                   │
└──────────────────────────────────┘

Adım 2: "+" basıldı
┌──────────────────────────────────┐
│              0                   │
└──────────────────────────────────┘

Adım 3: "37" girildi
┌──────────────────────────────────┐
│             37                   │
└──────────────────────────────────┘

Adım 4: "=" basıldı
┌──────────────────────────────────┐
│             62                   │  ← Sonuç
└──────────────────────────────────┘
```

### Senaryo 3: Trigonometrik İşlem (sin(30))
```
Adım 1: "30" girildi
┌──────────────────────────────────┐
│             30                   │
└──────────────────────────────────┘

Adım 2: "sin" basıldı
┌──────────────────────────────────┐
│  0.49999999999999994             │  ← Sonuç (derece cinsinden)
└──────────────────────────────────┘
```

### Senaryo 4: Karekök (√144)
```
Adım 1: "144" girildi
┌──────────────────────────────────┐
│            144                   │
└──────────────────────────────────┘

Adım 2: "√" basıldı
┌──────────────────────────────────┐
│            12.0                  │  ← Sonuç
└──────────────────────────────────┘
```

### Senaryo 5: Üslü Sayı (2^8)
```
Adım 1: "2" girildi
┌──────────────────────────────────┐
│              2                   │
└──────────────────────────────────┘

Adım 2: "xʸ" basıldı
┌──────────────────────────────────┐
│              0                   │
└──────────────────────────────────┘

Adım 3: "8" girildi
┌──────────────────────────────────┐
│              8                   │
└──────────────────────────────────┘

Adım 4: "=" basıldı
┌──────────────────────────────────┐
│            256                   │  ← Sonuç
└──────────────────────────────────┘
```

### Senaryo 6: Hata Durumu (Sıfıra Bölme)
```
Adım 1: "5 / 0" girildi ve "=" basıldı
┌──────────────────────────────────┐
│            Hata                  │
└──────────────────────────────────┘

┌────────────────────────────────────┐
│  ⚠️  Hata                     [X] │
│                                    │
│  Sıfıra bölme hatası               │
│                                    │
│           [ Tamam ]                │
└────────────────────────────────────┘
```

### Senaryo 7: Pi ve E Sabitleri
```
"π" basıldığında:
┌──────────────────────────────────┐
│  3.141592653589793               │
└──────────────────────────────────┘

"e" basıldığında:
┌──────────────────────────────────┐
│  2.718281828459045               │
└──────────────────────────────────┘
```

## Animasyon ve Etkileşim

### Buton Tıklama Efekti
1. **Normal Durum**: Hafif kabartılmış (Raised) görünüm
2. **Hover (Fare Üzerinde)**: Renk biraz açılır
3. **Basılı**: Buton aşağı iner (basılı görünüm)
4. **Bırakılınca**: Normal duruma döner

### Ekran Güncellemesi
- Sayılar girilirken: Sağdan sola eklenir
- Sonuç hesaplanırken: Anında güncellenir
- Hata durumunda: "Hata" yazısı görünür ve popup açılır

## Responsive Davranış

Hesap makinesi sabit boyutludur ve yeniden boyutlandırılamaz:
- **Genişlik**: 400px (sabit)
- **Yükseklik**: 600px (sabit)
- **Minimum boyut**: Yok (pencere sabit)
- **Maksimum boyut**: Yok (pencere sabit)

Bu, tutarlı bir kullanıcı deneyimi sağlar ve tüm butonların her zaman aynı yerde olmasını garantiler.

## Erişilebilirlik

### Renk Kontrastı
- Ekran: Koyu arkaplan (#1a1a1a) üzerinde parlak yeşil (#00ff00) - ✓ Yüksek kontrast
- Butonlar: Beyaz yazı (#ffffff) koyu arkaplan üzerinde - ✓ Okunabilir
- Turuncu butonlar: Beyaz yazı (#ffffff) turuncu arkaplan (#ff9500) - ✓ Okunabilir

### Font Boyutu
- Ekran: 24pt - ✓ Büyük ve okunabilir
- Butonlar: 14pt Bold - ✓ Net ve seçilebilir

### Buton Boyutu
- Her buton en az 5 karakter × 2 satır - ✓ Kolay tıklanabilir
- Butonlar arası 2px boşluk - ✓ Yanlış tıklamayı önler

## Tema Varyasyonları (Gelecek Sürümler için Öneriler)

### Klasik Tema
- Arkaplan: Beyaz
- Ekran: Siyah yazı, beyaz zemin
- Butonlar: Açık gri tonlar

### Yüksek Kontrast Tema
- Arkaplan: Siyah
- Ekran: Sarı yazı, siyah zemin
- Butonlar: Beyaz yazı, siyah arkaplan, kalın beyaz çerçeve

### Retro Tema
- Arkaplan: Kahverengi
- Ekran: Kırmızı LED yazı
- Butonlar: Kahverengi tonlar, vintage görünüm

## Teknik Detaylar

### Pencere Özellikleri
```python
- Başlık: "Bilimsel Hesap Makinesi"
- Boyut: 400x600 piksel
- Yeniden boyutlandırılabilir: Hayır (resizable=False)
- Arkaplan rengi: #2b2b2b
- Icon: Sistem varsayılanı (özelleştirilmemiş)
```

### Grid Düzeni
```python
- 6 satır × 5 sütun buton düzeni
- Her grid hücresi eşit ağırlıklı (weight=1)
- Hücreler arası 2px boşluk (padx=2, pady=2)
- Butonlar grid hücresini doldurur (sticky='nsew')
```

### Ekran Özellikleri
```python
- Widget tipi: tk.Entry (tek satırlı metin girişi)
- Font: ('Arial', 24, 'bold')
- Hizalama: justify='right'
- Çerçeve: bd=10
- Relief: SUNKEN
- Arkaplan: #1a1a1a
- Yazı rengi: #00ff00
- Cursor rengi: #00ff00
```

Bu tasarım modern, kullanıcı dostu ve profesyonel bir bilimsel hesap makinesi deneyimi sağlar.
