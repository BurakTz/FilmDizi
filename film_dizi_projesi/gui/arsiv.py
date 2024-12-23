import tkinter as tk
from tkinter import ttk,messagebox
from models.content import content
from gui.filtreleme_arayuzu import filtreleme_arayuzu

def arsivim(menü, nesneler):
    menü.withdraw()
    arsiv_penceresi = tk.Toplevel()
    arsiv_penceresi.title("Arşiv")
    arsiv_penceresi.geometry("750x400")  # Daha geniş bir pencere boyutu
    arsiv_penceresi.configure(bg="#121212")

    # Grid düzenini ayarla
    arsiv_penceresi.grid_rowconfigure(0, weight=1)  # Tablo için
    arsiv_penceresi.grid_rowconfigure(1, weight=0)  # Buton için
    arsiv_penceresi.grid_columnconfigure(0, weight=1)

    # Treeview stili
    style = ttk.Style()
    style.theme_use("clam")  # Tema seçimi
    style.configure("Treeview", background="#121212", foreground="white", fieldbackground="#121212")
    style.configure("Treeview.Heading", background="#E50914", foreground="white", font=("Helvetica", 10, "bold"))


    # Tablo sütunlarını tanımla
    sütunlar = ("Ad", "Kategori", "Tür", "Süre", "Durum", "Yıldız", "Notlar")
    tree = ttk.Treeview(arsiv_penceresi, columns=sütunlar, show="headings")

    # Sütun başlıklarını ekle
    for sütun in sütunlar:
        tree.heading(sütun, text=sütun)
        tree.column(sütun, anchor="center", width=100)

    # Nesneler listesini tabloya ekle
    for nesne in nesneler:
        tree.insert(
            "", "end",
            values=(nesne.ad, nesne.kategori, nesne.tür, nesne.süre, nesne.durum, nesne.yildiz, nesne.notlar)
        )

    # Treeview için bir Scrollbar ekle
    scrollbar = ttk.Scrollbar(arsiv_penceresi, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    # Tabloyu grid'e yerleştir
    tree.grid(row=0, column=0, sticky="nsew")#Tabloyu hücrenin tüm köşelerine (kuzey, güney, doğu, batı) yayar.
    scrollbar.grid(row=0, column=1, sticky="ns")  # Dikey scrollbar sağ tarafa

    filtre_buton = tk.Button(
    arsiv_penceresi,
    text="Filtreleme",
    bg="#E50914",
    fg="white",
    command=lambda: filtreleme_arayuzu(arsiv_penceresi, nesneler, tree),
    width=15
    )
    filtre_buton.grid(row=1, column=0, columnspan=2, pady=10, sticky="s")  # Alt tarafa ortala

    def sil(tree, nesneler):
        secilen=tree.selection()
        if not secilen:
           messagebox.showerror("Hata","Lutfen silmek için satir veya satirlari seciniz.")
           return
        
        silinen_adlar = []

        for id in secilen:
            degerler = tree.item(id,"values")
            silinecek_ad=degerler[0]
            silinen_adlar.append(silinecek_ad)
            nesneler = [n for n in nesneler if n.ad != silinecek_ad]
            tree.delete(id)
            
        messagebox.showinfo("Silme İşlemi", "Silinen içerikler: " + ", ".join(silinen_adlar))
        


    
    sil_buton = tk.Button(
    arsiv_penceresi,
    text="Sil",
    bg="#E50914",
    fg="white",
    command=lambda: sil(tree, nesneler),
    width=15
    )
    sil_buton.grid(row=1, column=0, pady=10, sticky="e")

    # Menüye dön butonu
    geri_buton = tk.Button(
        arsiv_penceresi,
        text="Menüye Dön",
        bg="#E50914",
        fg="white",
        width=15,
        command=lambda: geri_don(arsiv_penceresi, menü)
    )
    geri_buton.grid(row=1, column=0, sticky="sw", padx=10, pady=10)  # Sol alta hizala
    
    
    def geri_don(pencere, menü):
       pencere.destroy()
       menü.deiconify()
