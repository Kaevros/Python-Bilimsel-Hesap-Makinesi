#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bilimsel Hesap Makinesi
Python ve Tkinter kullanılarak geliştirilmiş bilimsel hesap makinesi uygulaması
"""

import tkinter as tk
from tkinter import messagebox
import math

class BilimselHesapMakinesi:
    def __init__(self, root):
        self.root = root
        self.root.title("Bilimsel Hesap Makinesi")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#2b2b2b')
        
        # Değişkenler
        self.current_value = ""
        self.previous_value = ""
        self.operator = ""
        self.power_mode = False
        
        # UI oluştur
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        """Hesap makinesi ekranını oluşturur"""
        # Çerçeve
        display_frame = tk.Frame(self.root, bg='#2b2b2b', pady=10)
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        # Ekran
        self.display = tk.Entry(
            display_frame,
            font=('Arial', 24, 'bold'),
            justify='right',
            bd=10,
            bg='#1a1a1a',
            fg='#00ff00',
            insertbackground='#00ff00',
            relief=tk.SUNKEN
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.display.insert(0, "0")
        
    def create_buttons(self):
        """Tüm butonları oluşturur"""
        button_frame = tk.Frame(self.root, bg='#2b2b2b')
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buton düzeni
        buttons = [
            ['sin', 'cos', 'tan', 'log', 'C'],
            ['√', 'x²', 'xʸ', '(', ')'],
            ['7', '8', '9', '/', '←'],
            ['4', '5', '6', '*', 'π'],
            ['1', '2', '3', '-', 'e'],
            ['0', '.', '=', '+', 'ANS']
        ]
        
        # Buton stilleri
        number_style = {'bg': '#404040', 'fg': 'white', 'activebackground': '#505050'}
        operator_style = {'bg': '#ff9500', 'fg': 'white', 'activebackground': '#ffad33'}
        function_style = {'bg': '#505050', 'fg': 'white', 'activebackground': '#606060'}
        special_style = {'bg': '#d4d4d2', 'fg': 'black', 'activebackground': '#e5e5e5'}
        
        # Butonları oluştur
        for row_idx, row in enumerate(buttons):
            for col_idx, button_text in enumerate(row):
                # Stil seçimi
                if button_text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                    style = number_style
                elif button_text in ['+', '-', '*', '/', '=']:
                    style = operator_style
                elif button_text in ['C', '←']:
                    style = special_style
                else:
                    style = function_style
                
                btn = tk.Button(
                    button_frame,
                    text=button_text,
                    font=('Arial', 14, 'bold'),
                    width=5,
                    height=2,
                    bd=2,
                    relief=tk.RAISED,
                    command=lambda x=button_text: self.on_button_click(x),
                    **style
                )
                btn.grid(row=row_idx, column=col_idx, padx=2, pady=2, sticky='nsew')
        
        # Grid yapılandırması
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, button):
        """Buton tıklama olayını işler"""
        try:
            if button == 'C':
                self.clear()
            elif button == '←':
                self.backspace()
            elif button == '=':
                self.calculate()
            elif button in ['+', '-', '*', '/']:
                self.set_operator(button)
            elif button == 'sin':
                self.calculate_sin()
            elif button == 'cos':
                self.calculate_cos()
            elif button == 'tan':
                self.calculate_tan()
            elif button == 'log':
                self.calculate_log()
            elif button == '√':
                self.calculate_sqrt()
            elif button == 'x²':
                self.calculate_square()
            elif button == 'xʸ':
                self.set_power_mode()
            elif button == 'π':
                self.insert_pi()
            elif button == 'e':
                self.insert_e()
            elif button == 'ANS':
                self.insert_ans()
            elif button in ['(', ')']:
                self.append_to_display(button)
            else:
                self.append_to_display(button)
        except Exception as e:
            self.show_error(f"Hata: {str(e)}")
    
    def append_to_display(self, value):
        """Ekrana değer ekler"""
        current = self.display.get()
        if current == "0" or current == "Hata":
            self.display.delete(0, tk.END)
            self.display.insert(0, value)
        else:
            self.display.insert(tk.END, value)
    
    def clear(self):
        """Ekranı temizler"""
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")
        self.current_value = ""
        self.previous_value = ""
        self.operator = ""
        self.power_mode = False
    
    def backspace(self):
        """Son karakteri siler"""
        current = self.display.get()
        if len(current) > 1:
            self.display.delete(len(current)-1, tk.END)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
    
    def set_operator(self, op):
        """Operatör ayarlar"""
        try:
            current = self.display.get()
            if current and current != "0":
                if self.previous_value and self.operator:
                    self.calculate()
                self.previous_value = self.display.get()
                self.operator = op
                self.display.delete(0, tk.END)
                self.display.insert(0, "0")
        except Exception as e:
            self.show_error("Geçersiz işlem")
    
    def set_power_mode(self):
        """Üslü sayı modunu ayarlar"""
        try:
            current = self.display.get()
            if current and current != "0":
                self.previous_value = self.display.get()
                self.operator = '**'
                self.power_mode = True
                self.display.delete(0, tk.END)
                self.display.insert(0, "0")
        except Exception as e:
            self.show_error("Geçersiz işlem")
    
    def calculate(self):
        """Hesaplama yapar"""
        try:
            if self.operator and self.previous_value:
                current = self.display.get()
                expr = f"{self.previous_value}{self.operator}{current}"
                result = eval(expr)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.last_result = result
                self.previous_value = ""
                self.operator = ""
                self.power_mode = False
        except ZeroDivisionError:
            self.show_error("Sıfıra bölme hatası")
        except Exception as e:
            self.show_error("Geçersiz ifade")
    
    def calculate_sin(self):
        """Sinüs hesaplar (derece cinsinden)"""
        try:
            value = float(self.display.get())
            result = math.sin(math.radians(value))
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.last_result = result
        except ValueError:
            self.show_error("Geçersiz sayı")
    
    def calculate_cos(self):
        """Kosinüs hesaplar (derece cinsinden)"""
        try:
            value = float(self.display.get())
            result = math.cos(math.radians(value))
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.last_result = result
        except ValueError:
            self.show_error("Geçersiz sayı")
    
    def calculate_tan(self):
        """Tanjant hesaplar (derece cinsinden)"""
        try:
            value = float(self.display.get())
            result = math.tan(math.radians(value))
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.last_result = result
        except ValueError:
            self.show_error("Geçersiz sayı")
    
    def calculate_log(self):
        """10 tabanında logaritma hesaplar"""
        try:
            value = float(self.display.get())
            if value <= 0:
                self.show_error("Log sadece pozitif sayılar için")
                return
            result = math.log10(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.last_result = result
        except ValueError:
            self.show_error("Geçersiz sayı")
    
    def calculate_sqrt(self):
        """Karekök hesaplar"""
        try:
            value = float(self.display.get())
            if value < 0:
                self.show_error("Negatif sayının karekökü alınamaz")
                return
            result = math.sqrt(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.last_result = result
        except ValueError:
            self.show_error("Geçersiz sayı")
    
    def calculate_square(self):
        """Kare hesaplar"""
        try:
            value = float(self.display.get())
            result = value ** 2
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.last_result = result
        except ValueError:
            self.show_error("Geçersiz sayı")
    
    def insert_pi(self):
        """Pi sayısını ekler"""
        self.display.delete(0, tk.END)
        self.display.insert(0, str(math.pi))
    
    def insert_e(self):
        """e sayısını ekler"""
        self.display.delete(0, tk.END)
        self.display.insert(0, str(math.e))
    
    def insert_ans(self):
        """Son sonucu ekler"""
        if hasattr(self, 'last_result'):
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.last_result))
    
    def show_error(self, message):
        """Hata mesajı gösterir"""
        self.display.delete(0, tk.END)
        self.display.insert(0, "Hata")
        messagebox.showerror("Hata", message)
        self.clear()

def main():
    """Ana uygulama başlatır"""
    root = tk.Tk()
    app = BilimselHesapMakinesi(root)
    root.mainloop()

if __name__ == "__main__":
    main()
