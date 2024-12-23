import tkinter as tk
from tkinter import ttk, messagebox
from models.content import content

def filmdizi_ekle(menü,nesneler):
    menü.withdraw()
    ekleme_penceresi = tk.Toplevel()
    ekleme_penceresi.title("Film Dizi Ekle")
    ekleme_penceresi.geometry("450x450")  # Daha geniş bir pencere boyutu
    ekleme_penceresi.configure(bg="#121212")

    for i in range(10): 
        ekleme_penceresi.grid_rowconfigure(i, weight=1)
    for j in range(2): 
        ekleme_penceresi.grid_columnconfigure(j, weight=1)


    baslik = tk.Label(
        ekleme_penceresi,
        text="Film ve Dizi Kaydı",
        bg="#121212",
        fg="#E50914",
        font=("Comic Sans MS", 25),
    )
    baslik.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

    alanlar = ["Ad", "Kategori", "Tür", "Süre", "Durum", "Yıldız", "Notlar"]

    entryler = {}
    comboboxlar = {}

    tür_secenekler = ["Film", "Dizi"]
    kategori_secenekler = ["Korku", "Komedi", "Dram", "Aksiyon", "Aşk", "Bilim Kurgu"]
    durum_secenekler = ["İzlenmedi", "İzleniyor", "İzlendi"]
    yildiz_secenekler = [str(i) for i in range(1, 6)]
    # Ad Alanı
    ad_label = tk.Label(ekleme_penceresi, text="Ad:", bg="#2C2C2C", fg="white", width=18, anchor="center", font=("Helvetica", 10, "bold"))
    ad_label.grid(row=2, column=0, padx=10, pady=5)
    ad_entry = tk.Entry(ekleme_penceresi, width=20)
    ad_entry.grid(row=2, column=1, padx=10, pady=5)

    # Kategori Alanı
    kategori_label = tk.Label(ekleme_penceresi, text="Kategori:", bg="#2C2C2C", fg="white", width=18, anchor="center", font=("Helvetica", 10, "bold"))
    kategori_label.grid(row=3, column=0, padx=10, pady=5)
    kategori_combobox = ttk.Combobox(ekleme_penceresi, width=17, state="readonly", values=kategori_secenekler)
    kategori_combobox.grid(row=3, column=1, padx=10, pady=5)

    # Tür Alanı
    tür_label = tk.Label(ekleme_penceresi, text="Tür:", bg="#2C2C2C", fg="white", width=18, anchor="center", font=("Helvetica", 10, "bold"))
    tür_label.grid(row=4, column=0, padx=10, pady=5)
    tür_combobox = ttk.Combobox(ekleme_penceresi, width=17, state="readonly", values=tür_secenekler)
    tür_combobox.grid(row=4, column=1, padx=10, pady=5)

    # Süre Alanı
    süre_label = tk.Label(ekleme_penceresi, text="Süre(dakika):", bg="#2C2C2C", fg="white", width=18, anchor="center", font=("Helvetica", 10, "bold"))
    süre_label.grid(row=5, column=0, padx=10, pady=5)
    süre_entry = tk.Entry(ekleme_penceresi, width=20)
    süre_entry.grid(row=5, column=1, padx=10, pady=5)
    

    # Durum Alanı
    durum_label = tk.Label(ekleme_penceresi, text="Durum:", bg="#2C2C2C", fg="white", width=18, anchor="center", font=("Helvetica", 10, "bold"))
    durum_label.grid(row=6, column=0, padx=10, pady=5)
    durum_combobox = ttk.Combobox(ekleme_penceresi, width=17, state="readonly", values=durum_secenekler)
    durum_combobox.grid(row=6, column=1, padx=10, pady=5)

    # Yıldız Alanı
    yildiz_label = tk.Label(ekleme_penceresi, text="Yıldız:", bg="#2C2C2C", fg="white", width=18, anchor="center", font=("Helvetica", 10, "bold"))
    yildiz_label.grid(row=7, column=0, padx=10, pady=5)
    yildiz_combobox = ttk.Combobox(ekleme_penceresi, width=17, state="readonly", values=yildiz_secenekler)
    yildiz_combobox.grid(row=7, column=1, padx=10, pady=5)

    # Notlar Alanı
    notlar_label = tk.Label(ekleme_penceresi, text="Notlar(Opsiyonel):", bg="#2C2C2C", fg="white", width=18, anchor="center", font=("Helvetica", 10, "bold"))
    notlar_label.grid(row=8, column=0, padx=10, pady=5)
    notlar_entry = tk.Entry(ekleme_penceresi, width=20)
    notlar_entry.grid(row=8, column=1, padx=10, pady=5)
    

    def kaydet():
        
        ad=ad_entry.get()
        if ad=="":
            messagebox.showerror("Hata","Ad kısmını doldurunuz")
            return
        kategori=kategori_combobox.get()
        if kategori=="":
            messagebox.showerror("Hata","Kategori kısmını doldurunuz")
            return
        tür=tür_combobox.get()
        if tür=="":
            messagebox.showerror("Hata","Tür kısmını doldurunuz")
            return
        süre=süre_entry.get()
        if süre=="":
            messagebox.showerror("Hata","Süre kısmını doldurunuz")
            return
        if süre.isdigit():
           süre = int(süre)  
        else:
           messagebox.showerror("Hata", "Lütfen geçerli bir tam sayı giriniz!")
           return
        durum=durum_combobox.get()
        if durum=="":
            messagebox.showerror("Hata","Durum kısmını doldurunuz")
            return
        yildiz=yildiz_combobox.get()
        if yildiz=="":
            messagebox.showerror("Hata","Yıldız kısmını doldurunuz")
            return
        yildiz=int(yildiz)
        notlar=notlar_entry.get()
        yeni_nesne = content(ad, kategori, tür, süre, durum, yildiz, notlar)

        for n in nesneler:
          if n.ad == ad:  
              messagebox.showerror("Hata",f"{tür} zaten listede mevcut.")
              return 

    
        nesneler.append(yeni_nesne)
        messagebox.showinfo("Bilgi",f"{tür} listeye başariyla eklenmistir")
   
        for n in nesneler:
          print(n)



    kaydet_buton = tk.Button(
    ekleme_penceresi,
    text="KAYDET",
    command=kaydet,
    bg="#E50914",
    fg="white",
    width=15,
    )
    kaydet_buton.grid(row=9, column=1, padx=70, pady=5, sticky="e")

    geri_buton = tk.Button(
        ekleme_penceresi,
        text="Menüye Dön",
        command=lambda: geri_don(ekleme_penceresi, menü),
        bg="#E50914",
        fg="white",
        width=15,
    )
    geri_buton.grid(row=10, column=0, padx=10, pady=10, sticky="sw")


    def geri_don(pencere,menü):
      pencere.destroy()
      menü.deiconify()
