import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import sys


# Pencere oluşturun
root = tk.Tk()
root.geometry("600x700+300+100")
root.title("Takım İstatistikleri")


class MyCustomError(Exception):
    pass

# Takım 1 için girdi alanları
t1_label = tk.Label(root, text="Takım 1:")
t1_label.grid(row=1, column=0)

t1_ad_label = tk.Label(root, text="Takım Adını Giriniz:")
t1_ad_label.grid(row=5, column=0)
t1_ad_entry = tk.Entry(root)
t1_ad_entry.grid(row=5, column=1)

t1_şut_label = tk.Label(root, text="Toplam Şut Sayısı:")
t1_şut_label.grid(row=6, column=0)
t1_şut_entry = tk.Entry(root)
t1_şut_entry.grid(row=6, column=1)

t1_isabet_şut_label = tk.Label(root, text="İsabetli Şut Sayısı:")
t1_isabet_şut_label.grid(row=7, column=0)
t1_isabet_şut_entry = tk.Entry(root)
t1_isabet_şut_entry.grid(row=7, column=1)

t1_top_oynama_label = tk.Label(root, text="Topla Oynama Yüzdesi:")
t1_top_oynama_label.grid(row=8, column=0)
t1_top_oynama_entry = tk.Entry(root)
t1_top_oynama_entry.grid(row=8, column=1)

t1_pas_sayı_label = tk.Label(root, text="Pas Sayısı:")
t1_pas_sayı_label.grid(row=9,column=0)
t1_pas_sayı_entry = tk.Entry(root)
t1_pas_sayı_entry.grid(row=9,column=1)

t1_pas_isabet_label = tk.Label(root, text="Pas İsabet Yüzdesi:")
t1_pas_isabet_label.grid(row=10,column=0)
t1_pas_isabet_entry = tk.Entry(root)
t1_pas_isabet_entry.grid(row=10,column=1)

t1_faul_label = tk.Label(root, text="Faul Sayısı:")
t1_faul_label.grid(row=11,column=0)
t1_faul_entry = tk.Entry(root)
t1_faul_entry.grid(row=11,column=1)

# Takım 2 için girdi alanları
t2_label = tk.Label(root, text="Takım 2:")
t2_label.grid(row=1, column=5)

t2_ad_label = tk.Label(root, text="Takım Adını Giriniz:")
t2_ad_label.grid(row=5, column=6)
t2_ad_entry = tk.Entry(root)
t2_ad_entry.grid(row=5, column=7)

t2_şut_label = tk.Label(root, text="Toplam Şut Sayısı:")
t2_şut_label.grid(row=6, column=6)
t2_şut_entry = tk.Entry(root)
t2_şut_entry.grid(row=6, column=7)

t2_isabet_şut_label = tk.Label(root, text="İsabetli Şut Sayısı:")
t2_isabet_şut_label.grid(row=7, column=6)
t2_isabet_şut_entry = tk.Entry(root)
t2_isabet_şut_entry.grid(row=7, column=7)

t2_top_oynama_label = tk.Label(root, text="Topla Oynama Yüzdesi:")
t2_top_oynama_label.grid(row=8, column=6)
t2_top_oynama_entry = tk.Entry(root)
t2_top_oynama_entry.grid(row=8, column=7)

t2_pas_sayı_label = tk.Label(root, text="Pas Sayısı:")
t2_pas_sayı_label.grid(row=9,column=6)
t2_pas_sayı_entry = tk.Entry(root)
t2_pas_sayı_entry.grid(row=9,column=7)

t2_pas_isabet_label = tk.Label(root, text="Pas İsabet Yüzdesi:")
t2_pas_isabet_label.grid(row=10,column=6)
t2_pas_isabet_entry = tk.Entry(root)
t2_pas_isabet_entry.grid(row=10,column=7)

t2_faul_label = tk.Label(root, text="Faul Sayısı:")
t2_faul_label.grid(row=11,column=6)
t2_faul_entry = tk.Entry(root)
t2_faul_entry.grid(row=11,column=7)


# İşlevi tanımlayın
def draw_graph():
    
    t1_şut = int(t1_şut_entry.get())
    t2_şut = int(t2_şut_entry.get())
    
    t1_isabet_şut = int(t1_isabet_şut_entry.get())
    t2_isabet_şut = int(t2_isabet_şut_entry.get())
    
    t1_top_oynama = int(t1_top_oynama_entry.get())
    t2_top_oynama = int(t2_top_oynama_entry.get())
    
    t1_pas_sayı = int(t1_pas_sayı_entry.get())
    t2_pas_sayı = int(t2_pas_sayı_entry.get())
    
    t1_pas_isabet = int(t1_pas_isabet_entry.get())
    t2_pas_isabet = int(t2_pas_isabet_entry.get())
            
    t1_faul = int(t1_faul_entry.get())
    t2_faul = int(t2_faul_entry.get())
    
    # Verileri bir liste halinde tutalım
    top_şut = [t1_şut, t2_şut]
    top_isabet = [t1_isabet_şut,t2_isabet_şut]
    top_oynama = [t1_top_oynama,t2_top_oynama]
    top_pas = [t1_pas_sayı,t2_pas_sayı]
    top_pasIsabet = [t1_pas_isabet,t2_pas_isabet]
    top_faul = [t1_faul,t2_faul]
    
    
   
    # Etiketleri de bir liste halinde tutalım
    labels = [t1_ad_entry.get(), t2_ad_entry.get()]

    fig, axs = plt.subplots(2,3)    

    # Pasta grafiğini çizdirelim1
    axs[0,0].pie(top_şut, labels=labels, autopct='%1.1f')
    axs[0,0].set_title("Toplam Şut Sayısı")
    
    axs[0,1].pie(top_isabet, labels=labels, autopct='%1.1f')
    axs[0,1].set_title("Şut İsabet Yüzdesi")
    
    axs[0,2].pie(top_oynama, labels=labels, autopct='%1.1f')
    axs[0,2].set_title("Topla Oynama Yüzdesi")
    
    axs[1,0].pie(top_pas, labels=labels, autopct='%1.1f')
    axs[1,0].set_title("Toplam Pas Sayısı")
    
    axs[1,1].pie(top_pasIsabet, labels=labels, autopct='%1.1f')
    axs[1,1].set_title("Pas İsabet Yüzdesi")
    
    axs[1,2].pie(top_faul, labels=labels, autopct='%1.1f')
    axs[1,2].set_title("Faul Oranı")
    
    if t1_top_oynama + t2_top_oynama != 100:
        plt.close()
        messagebox.showwarning("Hata","İki Takımın Topla Oynama Yüzdesi 100 olmalı")
    elif t1_pas_isabet>100 or t2_pas_isabet>100:
        plt.close()
        messagebox.showwarning("Hata","Pas İsabet Yüzdesi 100'den fazla olamaz")
    elif t2_pas_isabet>100:
        plt.close()
    else:
        plt.show()
        
    

# Grafik çizme düğmesini ekleyin

button = tk.Button(root, text="Grafik Çiz", command=draw_graph)

button.grid(row=15, column=7, columnspan=5)

root.mainloop()
root.destroy()

