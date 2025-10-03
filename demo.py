#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bilimsel Hesap Makinesi Demo
Hesap makinesinin yeteneklerini gösteren demo script
"""

import math

def print_header(title):
    """Başlık yazdırır"""
    print("\n" + "="*50)
    print(f"  {title}")
    print("="*50)

def demo_basic_operations():
    """Temel işlemleri gösterir"""
    print_header("TEMEL ARİTMETİK İŞLEMLER")
    
    operations = [
        ("15 + 27", 15 + 27),
        ("100 - 37", 100 - 37),
        ("12 × 8", 12 * 8),
        ("144 ÷ 12", 144 / 12),
        ("(5 + 3) × 2", (5 + 3) * 2),
    ]
    
    for expr, result in operations:
        print(f"  {expr:20} = {result}")

def demo_scientific_functions():
    """Bilimsel fonksiyonları gösterir"""
    print_header("BİLİMSEL FONKSİYONLAR")
    
    print("\n📐 Trigonometrik Fonksiyonlar (Derece):")
    trig = [
        ("sin(30°)", math.sin(math.radians(30))),
        ("cos(60°)", math.cos(math.radians(60))),
        ("tan(45°)", math.tan(math.radians(45))),
        ("sin(90°)", math.sin(math.radians(90))),
    ]
    for expr, result in trig:
        print(f"  {expr:20} = {result:.6f}")
    
    print("\n📊 Logaritma ve Üslü Sayılar:")
    log_pow = [
        ("log₁₀(100)", math.log10(100)),
        ("log₁₀(1000)", math.log10(1000)),
        ("2⁸", 2 ** 8),
        ("5³", 5 ** 3),
        ("10⁴", 10 ** 4),
    ]
    for expr, result in log_pow:
        print(f"  {expr:20} = {result}")
    
    print("\n√ Karekök ve Kare:")
    sqrt_sq = [
        ("√16", math.sqrt(16)),
        ("√144", math.sqrt(144)),
        ("5²", 5 ** 2),
        ("12²", 12 ** 2),
    ]
    for expr, result in sqrt_sq:
        print(f"  {expr:20} = {result}")

def demo_special_values():
    """Özel değerleri gösterir"""
    print_header("ÖZEL DEĞERLER VE SABİTLER")
    
    print(f"\n  π (Pi)               = {math.pi:.10f}")
    print(f"  e (Euler)            = {math.e:.10f}")
    print(f"  2π                   = {2 * math.pi:.10f}")
    print(f"  π/2                  = {math.pi / 2:.10f}")
    print(f"  e²                   = {math.e ** 2:.10f}")

def demo_complex_calculations():
    """Karmaşık hesaplamaları gösterir"""
    print_header("KARMAŞIK HESAPLAMALAR")
    
    print("\n🔢 Fizik Formülleri:")
    
    # Çemberin alanı: A = πr²
    r = 5
    area = math.pi * r ** 2
    print(f"  Çemberin alanı (r=5):")
    print(f"  A = πr² = π×{r}² = {area:.2f}")
    
    # Serbest düşüş: h = ½gt²
    g = 9.8
    t = 3
    h = 0.5 * g * t ** 2
    print(f"\n  Serbest düşüş (t=3s):")
    print(f"  h = ½gt² = ½×{g}×{t}² = {h:.2f} m")
    
    # Pisagor teoremi: c = √(a² + b²)
    a, b = 3, 4
    c = math.sqrt(a ** 2 + b ** 2)
    print(f"\n  Pisagor (a=3, b=4):")
    print(f"  c = √(a² + b²) = √({a}² + {b}²) = {c:.2f}")
    
    print("\n📈 İstatistik:")
    
    # Ortalama ve standart sapma hesabı
    numbers = [10, 20, 30, 40, 50]
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    print(f"  Sayılar: {numbers}")
    print(f"  Ortalama: {mean:.2f}")
    print(f"  Standart Sapma: {std_dev:.2f}")

def demo_real_world_examples():
    """Gerçek dünya örnekleri"""
    print_header("GERÇEK DÜNYA ÖRNEKLERİ")
    
    print("\n🏗️ İnşaat Mühendisliği:")
    # Eğim açısı hesabı
    height = 10  # metre
    distance = 20  # metre
    angle_rad = math.atan(height / distance)
    angle_deg = math.degrees(angle_rad)
    print(f"  Yükseklik: {height}m, Mesafe: {distance}m")
    print(f"  Eğim açısı: {angle_deg:.2f}°")
    
    print("\n🌡️ Fizik:")
    # Kinetik enerji: E = ½mv²
    m = 2  # kg
    v = 10  # m/s
    E = 0.5 * m * v ** 2
    print(f"  Kütle: {m}kg, Hız: {v}m/s")
    print(f"  Kinetik Enerji: E = ½mv² = {E:.2f} J")
    
    print("\n💰 Finans:")
    # Bileşik faiz: A = P(1 + r)^t
    P = 1000  # Ana para
    r = 0.05  # Yıllık faiz (%5)
    t = 10  # Yıl
    A = P * (1 + r) ** t
    print(f"  Ana para: {P}₺, Faiz: %{r*100}, Süre: {t} yıl")
    print(f"  Toplam: A = P(1+r)^t = {A:.2f}₺")
    
    print("\n🌍 Coğrafya:")
    # İki nokta arası mesafe (basitleştirilmiş)
    lat1, lon1 = 41.0082, 28.9784  # İstanbul
    lat2, lon2 = 39.9334, 32.8597  # Ankara
    # Yaklaşık hesaplama
    dlat = abs(lat2 - lat1)
    dlon = abs(lon2 - lon1)
    distance_approx = math.sqrt(dlat**2 + dlon**2) * 111  # km (yaklaşık)
    print(f"  İstanbul - Ankara yaklaşık mesafe:")
    print(f"  ~{distance_approx:.0f} km")

def main():
    """Tüm demoları çalıştırır"""
    print("\n" + "╔" + "="*48 + "╗")
    print("║  BİLİMSEL HESAP MAKİNESİ DEMO               ║")
    print("║  Yetenekler ve Kullanım Örnekleri          ║")
    print("╚" + "="*48 + "╝")
    
    demo_basic_operations()
    demo_scientific_functions()
    demo_special_values()
    demo_complex_calculations()
    demo_real_world_examples()
    
    print_header("DEMO TAMAMLANDI")
    print("\n✨ Hesap makinesini çalıştırmak için:")
    print("   python3 hesap_makinesi.py\n")
    print("📚 Daha fazla bilgi için:")
    print("   KULLANIM.md dosyasına bakın\n")

if __name__ == "__main__":
    main()
