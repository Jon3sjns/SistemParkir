dict_data = []

def cek_plat(inp_plat):
    for data in dict_data:
        if inp_plat == data["plat"]:
            return False
    return True

def simpan_masuk(inp_plat, inp_waktuMasuk):
    if cek_plat(inp_plat):
        dict_data.append({"plat": inp_plat, "waktu_masuk": inp_waktuMasuk})
        return True
    else:
        return False

def hitung_keluar(inp_plat, waktu_keluar):
    for data in dict_data:
        if data["plat"] == inp_plat:
            hitung_biaya = int(waktu_keluar)-int(data["waktu_masuk"])
            dict_data.remove(data)
            return "Total biaya plat " + inp_plat + " : "+str(hitung_biaya*2000).replace("-","")
    return False


while True:
    print("""===================================
+     Sistem parkir sederhana     +
===================================""")
    print("1. Masuk\n2. Keluar\n3. Cek semua kendaraan\n99. Keluar")
    try:
        inp_pilih = int(input("Masukan angka: "))

        if inp_pilih == 1:  # Parkir masuk
            inp_plat = input("Masukan plat nomor: ")
            inp_waktuMasuk = input("Masukan waktu sekarang(jam): ")
            simpan = simpan_masuk(inp_plat, inp_waktuMasuk)
            if not simpan:
                print("Plat sudah tersedia!")
            else:
                print("Plat", inp_plat, "tersimpan!")

        elif inp_pilih == 2: # Parkir keluar
            inp_plat = input("Masukan plat nomor: ")
            inp_waktuKeluar = input("Masukan waktu sekarang(jam): ")
            keluar = hitung_keluar(inp_plat, inp_waktuKeluar)
            if keluar:
                print(keluar)
            else:
                print("Plat tidak ditemukan!")

        elif inp_pilih == 3: # Tampilkan semua kendaraan
            if dict_data:
                print("="*46)
                print("+"," "*5, "Plat", " "*5, "+"," "*5,"Waktu masuk"," "*5,"+")
                print("="*46)
                for i in dict_data:
                    #print("-"*46)
                    print("+"," "*5, i["plat"], " "*5, "+"," "*9, i["waktu_masuk"]," "*8,"+")
                    print("-"*46)
            else:
                print("Data kendaraan tidak ada!!!")

        elif inp_pilih == 99: #Keluar
            break
            
    except ValueError:
        print("Harus memasukan angka!")
