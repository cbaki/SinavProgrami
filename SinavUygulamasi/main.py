import threading

def sinav():
    print("Sınav programına hoşgeldiniz.")
    print("\n***Kurallar***")
    print("1)Cevap vermek için sadece şık yazınız. (Örnek Cevap: a)\n2)Boş geçmek için sadece #Enter# tuşuna basınız.\n3)Her soru 10 puandır.\n4)Yanlış doğruyu götürmez.\n5)Sınav süresi 10 dakikadır.\n\n\n ")

    sorular = [
        {
            "soru": "2 GB kaç MB eder?\na)256\nb)512\nc)1024\nd)2056",
            "cevap": "d"
        },
        {
            "soru": "Aşağıdakilerden hangisi donanım parçalarından biri değildir?\na)Klavye\nb)Mouse\nc)Kasa\nd)Windows",
            "cevap": "d"
        },
        {
            "soru": "Ana belleğin sadece okunabilen, silinemeyen ve değiştirilemeyen kısmına ne ad verilir?\na)RAM Bellek\nb)ROM Bellek\nc)Hard Disk\nd)Cpu",
            "cevap": "b"
        },
        {
            "soru": "Aşağıdakilerden hangisi giriş birimidir?\na)Ekran\nb)Fare\nc)Yazıcı\nd)Hoparlör",
            "cevap": "b"
        },
        {
            "soru": "Aşağıdakilerden hangisi çıkış birimidir?\na)Oyun Çubuğu\nb)Ekran\nc)Yazıcı\nd)Optik Okuyucu",
            "cevap": "c"
        },
        {
            "soru": "Aşağıdakilerden hangisi depolama birimi değildir?\na)Sabit Disk\nb)RAM\nc)ROM\nd)Anakart",
            "cevap": "d"
        },
        {
            "soru": "Aşağıdakilerden hangisi doğrudur?\na)1 Kilobyte = 8 Bit\nb)1024 MB = 1 KB\nc)1 KB = 1024 Byte\nd)1 GB - 1024 KB",
            "cevap": "c"
        },
        {
            "soru": "I. Klavye                II. Fare                     III. Yazıcı                   IV. Tarayıcı\nYukarıdakilerden hangisi giriş birimidir?\na) I,II\nb)I,II,III\nc)I,II,IV\nd)I,IV",
            "cevap": "c"
        },
        {
            "soru": "Hangisi bir sorgulama dilidir?\na)SQL\nb)Python\nc)JavaScript\nd)C#",
            "cevap": "a"
        },
        {
            "soru": "Algoritma şemasında bilgi giriş çıkışı için kullanılan sembol hangisidir?\na)Elips\nb)Dikdörtgen\nc)Paralel Kenar\nd)Eşkenar Dörtgen",
            "cevap": "c"
        }
    ]

    puan = 0

    cevap_anahtari = {
        1: 'D',
        2: 'D',
        3: 'B',
        4: 'B',
        5: 'C',
        6: 'D',
        7: 'C',
        8: 'C',
        9: 'A',
        10:'C'
    }

    for i in sorular:
        print(i["soru"])
        while True:
            cevap = input("Cevap: ")
            if cevap.lower() in ['a', 'b', 'c', 'd', ""]:
                break
            else:
                print("Geçersiz cevap! Lütfen yalnızca 'a', 'b', 'c' veya 'd' seçeneklerinden birini girin. Boş geçmek için #Enter# basın.")
        if cevap.lower() == i["cevap"].lower():
            print("Doğru cevap")
            puan += 10
            cevap_anahtari[sorular.index(i)+1] = i["cevap"].upper()
        elif cevap.strip() == "":
            print("Boş cevap")
            cevap_anahtari[sorular.index(i)+1] = i["cevap"].lower()
        else:
            cevap_anahtari[sorular.index(i)+1] = i["cevap"].lower()

    print("Sınav bitti.")
    print("Puanınız:", puan)

    if puan >= 50:
        print("Tebrikler, başarılı oldunuz.")
    else:
        print("Başarısız oldunuz.")

    print("Cevap Anahtarı:")
    for i in cevap_anahtari:
        if cevap_anahtari[i].isupper():
            print(f"{i}. {cevap_anahtari[i]}")
        else:
            print(f"{i}. {cevap_anahtari[i].lower()}")

def timer():
    print("Sınav süresi doldu!")
    exit()

t = threading.Timer(600.0, timer)
t.start()
sinav()
t.cancel()