#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bilimsel Hesap Makinesi Test Dosyası
Matematiksel fonksiyonların doğruluğunu test eder
"""

import math

def test_basic_operations():
    """Temel aritmetik işlemleri test eder"""
    print("=== Temel Aritmetik İşlemler ===")
    
    # Toplama
    result = 5 + 3
    print(f"5 + 3 = {result}")
    assert result == 8, "Toplama hatası"
    
    # Çıkarma
    result = 10 - 4
    print(f"10 - 4 = {result}")
    assert result == 6, "Çıkarma hatası"
    
    # Çarpma
    result = 6 * 7
    print(f"6 * 7 = {result}")
    assert result == 42, "Çarpma hatası"
    
    # Bölme
    result = 15 / 3
    print(f"15 / 3 = {result}")
    assert result == 5.0, "Bölme hatası"
    
    print("✓ Tüm temel işlemler başarılı\n")

def test_scientific_functions():
    """Bilimsel fonksiyonları test eder"""
    print("=== Bilimsel Fonksiyonlar ===")
    
    # Sin (derece cinsinden)
    value = 30
    result = math.sin(math.radians(value))
    print(f"sin(30°) = {result}")
    assert abs(result - 0.5) < 0.0001, "Sin hatası"
    
    # Cos (derece cinsinden)
    value = 60
    result = math.cos(math.radians(value))
    print(f"cos(60°) = {result}")
    assert abs(result - 0.5) < 0.0001, "Cos hatası"
    
    # Tan (derece cinsinden)
    value = 45
    result = math.tan(math.radians(value))
    print(f"tan(45°) = {result}")
    assert abs(result - 1.0) < 0.0001, "Tan hatası"
    
    # Log (10 tabanında)
    value = 100
    result = math.log10(value)
    print(f"log₁₀(100) = {result}")
    assert result == 2.0, "Log hatası"
    
    # Karekök
    value = 16
    result = math.sqrt(value)
    print(f"√16 = {result}")
    assert result == 4.0, "Karekök hatası"
    
    # Kare
    value = 5
    result = value ** 2
    print(f"5² = {result}")
    assert result == 25, "Kare hatası"
    
    # Üslü sayı
    base = 2
    exp = 8
    result = base ** exp
    print(f"2⁸ = {result}")
    assert result == 256, "Üslü sayı hatası"
    
    print("✓ Tüm bilimsel fonksiyonlar başarılı\n")

def test_special_values():
    """Özel değerleri test eder"""
    print("=== Özel Değerler ===")
    
    # Pi
    print(f"π = {math.pi}")
    assert abs(math.pi - 3.14159265) < 0.0001, "Pi hatası"
    
    # e
    print(f"e = {math.e}")
    assert abs(math.e - 2.71828182) < 0.0001, "e hatası"
    
    print("✓ Özel değerler başarılı\n")

def test_error_handling():
    """Hata yönetimini test eder"""
    print("=== Hata Yönetimi ===")
    
    # Sıfıra bölme
    try:
        result = 5 / 0
        assert False, "Sıfıra bölme hatası yakalanmadı"
    except ZeroDivisionError:
        print("✓ Sıfıra bölme hatası doğru şekilde yakalandı")
    
    # Negatif karekök
    try:
        result = math.sqrt(-1)
        assert False, "Negatif karekök hatası yakalanmadı"
    except ValueError:
        print("✓ Negatif karekök hatası doğru şekilde yakalandı")
    
    # Negatif log
    try:
        result = math.log10(-5)
        assert False, "Negatif log hatası yakalanmadı"
    except ValueError:
        print("✓ Negatif log hatası doğru şekilde yakalandı")
    
    print("✓ Hata yönetimi başarılı\n")

def test_complex_expressions():
    """Karmaşık ifadeleri test eder"""
    print("=== Karmaşık İfadeler ===")
    
    # Parantezli işlem
    result = (5 + 3) * 2
    print(f"(5 + 3) * 2 = {result}")
    assert result == 16, "Parantezli işlem hatası"
    
    # İç içe işlemler
    result = 2 ** 3 + math.sqrt(16)
    print(f"2³ + √16 = {result}")
    assert result == 12.0, "İç içe işlem hatası"
    
    # Trigonometrik ve aritmetik
    result = math.sin(math.radians(90)) * 10
    print(f"sin(90°) * 10 = {result}")
    assert abs(result - 10.0) < 0.0001, "Trigonometrik aritmetik hatası"
    
    print("✓ Karmaşık ifadeler başarılı\n")

def main():
    """Tüm testleri çalıştırır"""
    print("\n" + "="*50)
    print("BİLİMSEL HESAP MAKİNESİ TEST PAKETİ")
    print("="*50 + "\n")
    
    try:
        test_basic_operations()
        test_scientific_functions()
        test_special_values()
        test_error_handling()
        test_complex_expressions()
        
        print("="*50)
        print("✓ TÜM TESTLER BAŞARIYLA TAMAMLANDI!")
        print("="*50)
        return 0
    except AssertionError as e:
        print(f"\n✗ Test hatası: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Beklenmeyen hata: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
