import mata_uang.kurs_mata_uang

def main():

    print("<--------------------------------->")
    print("<| Kalkulator Konversi Mata Uang |>")
    print("<--------------------------------->")
    print("| Silahkan Pilih Mata Uang        |")
    print("| 1.Rupiah                        |")
    print("| 2.Dollar Amerika                |")
    print("| 3.Dollar Australia              |")
    print("| 4.Dirham                        |")
    print("<--------------------------------->")
    i = "ya";
    try:
        a = int(input("| Pilihan Pertama : "))
        b = int(input("| Pilihan Kedua   : "))
        if a == 1 and b == 2:
            print("<--------------------------------->")
            print("<|  Rupiah --> Dollar Amerika    |>")
            print("<--------------------------------->")
            rp = float(input("\n<> Rp"))
            dlr = mata_uang.kurs_mata_uang.rupiahdollar(rp)
            print("\n<-> Hasil konversi : $ ",dlr)
        elif a == 1 and b == 3:
            print("<--------------------------------->")
            print("<|  Rupiah --> Dollar Australia  |>")
            print("<--------------------------------->")
            rp = float(input("\n<> Rp"))
            dls = mata_uang.kurs_mata_uang.rupiahdolaus(rp)
            print("\n<-> Hasil konversi : $ ",dls)
        elif a == 1 and b == 4:
            print("<--------------------------------->")
            print("<|      Rupiah --> Dirham        |>")
            print("<--------------------------------->")
            rp = float(input("\n<> Rp"))
            drm = mata_uang.kurs_mata_uang.rupiahdirham(rp)
            print("\n<-> Hasil konversi : AED ",drm)
        elif a == 2 and b == 1:
            print("<--------------------------------->")
            print("<|   Dollar Amerika --> Rupiah   |>")
            print("<--------------------------------->")
            dlr = float(input("\n<> $"))
            rp = mata_uang.kurs_mata_uang.dollarrupiah(dlr)
            print("\n<-> Hasil konversi : Rp ",rp)
        elif a == 2 and b == 3:
            print("<------------------------------------->")
            print("<|Dollar Amerika --> Dollar Australia|>")
            print("<------------------------------------->")
            dlr = float(input("\n<> $"))
            dls = mata_uang.kurs_mata_uang.dollardolaus(dlr)
            print("\n<-> Hasil konversi : $ ",dls)
        elif a == 2 and b == 4:
            print("<--------------------------------->")
            print("<|   Dollar Amerika --> Dirham   |>")
            print("<--------------------------------->")
            dlr = float(input("\n<> $"))
            drm = mata_uang.kurs_mata_uang.dollardirham(dlr)
            print("\n<-> Hasil konversi : AED ",drm)
        elif a == 3 and b == 1:
            print("<--------------------------------->")
            print("<|  Dollar Australia --> Rupiah  |>")
            print("<--------------------------------->")
            dls = float(input("\n<> $"))
            rp = mata_uang.kurs_mata_uang.dolausrupiah(dls)
            print("\n<-> Hasil konversi : Rp ",rp)
        elif a == 3 and b == 2:
            print("<------------------------------------->")
            print("<|Dollar Australia --> Dollar Amerika|>")
            print("<------------------------------------->")
            dls = float(input("\n<> $"))
            dlr = mata_uang.kurs_mata_uang.dolausdollar(dls)
            print("\n<-> Hasil konversi : $ ",dlr)
        elif a == 3 and b == 4:
            print("<--------------------------------->")
            print("<| Dollar Australia --> Dirham   |>")
            print("<--------------------------------->")
            dls = float(input("\n<> $"))
            drm = mata_uang.kurs_mata_uang.dolausdirham(dls)
            print("\n<-> Hasil konversi : AED ",drm)
        elif a == 4 and b == 1:
            print("<--------------------------------->")
            print("<|      Dirham --> Rupiah        |>")
            print("<--------------------------------->")
            drm = float(input("\n<> AED "))
            rp = mata_uang.kurs_mata_uang.dirhamrupiah(drm)
            print("\n<-> Hasil konversi : Rp ",rp)
        elif a == 4 and b == 2:
            print("<------------------------------------->")
            print("<|    Dirham --> Dollar Amerika      |>")
            print("<------------------------------------->")
            drm = float(input("\n<> AED "))
            dlr = mata_uang.kurs_mata_uang.dirhamdollar(drm)
            print("\n<-> Hasil konversi : $ ",dlr)
        elif a == 4 and b == 3:
            print("<--------------------------------->")
            print("<| Dirham --> Dollar Australia   |>")
            print("<--------------------------------->")
            drm = float(input("\n<> AED "))
            dls = mata_uang.kurs_mata_uang.dirhamdolaus(drm)
            print("\n<-> Hasil konversi : $ ",dls)
        else :
            print(" Maaf,Kami tidak bisa mengkonversikannya ")
    except ValueError:
        print("Mohon untuk Memilih mata uangnya!!")
        
    
    lagi = str(input("\nMasih ingin konversi mata uang?[ya/tidak] : "))
    if lagi == "ya":
        return main()
    else:
        print("\nTerima kasih telah menggunakan jasa kami !!!")
    
    
if __name__ == "__main__":
    main()
