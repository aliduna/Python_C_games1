import random
import time
from datetime import datetime


SANS_MODU_IHTIMALI = 55

SANS_MODLARI = [
    "Cehennem", "Yanık Köprü", "Melek", "Efsane", "İmkansız",
    "Görünmez", "Sıcak Soğuk", "Ters Dünya", "Mayın Tarlası",
    "Çifte Zafer", "Kaçan Hedef", "Kaymış İpucu", "Tek Şans",
    "Yakın Atış", "Üç Can", "Yasaklı Rakam", "İki Hedef",
    "Süreye Karşı", "Asal Avı",
]

AYLAR = [
    "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
    "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık",
]


def cizgi():
    print("\n" + "=" * 52)

def tarihi_goster():
    simdi = datetime.now()
    ay_adi = AYLAR[simdi.month - 1]
    print(f"Tarih: {simdi.day} {ay_adi} {simdi.year} | Saat: {simdi:%H:%M}")


def sayi_al(metin, alt_sinir, ust_sinir):
    """Kullanıcıdan belirtilen aralıkta geçerli bir tam sayı alır."""
    while True:
        try:
            sayi = int(input(metin))
            if alt_sinir <= sayi <= ust_sinir:
                return sayi
            print(f"Lütfen {alt_sinir} ile {ust_sinir} arasında bir sayı gir.")
        except ValueError:
            print("Lütfen sadece tam sayı gir.")


def tahmin_al(alt_sinir, ust_sinir, gizli_sayi=None):
    """Tahmin veya oyun kontrolü alır: s = tur atla, q = çıkış."""
    while True:
        giris = input("\nTahminin (s: turu atla, q: çıkış): ").strip().lower()

        if giris in ("s", "q"):
            return giris

        try:
            sayi = int(giris)
            if alt_sinir <= sayi <= ust_sinir:
                return sayi
            print(f"Lütfen {alt_sinir} ile {ust_sinir} arasında bir sayı gir.")
        except ValueError:
            print("Lütfen sayı, 's' veya 'q' gir.")


def ana_mod_sec():
    cizgi()
    print("                ANA MODUNU SEÇ")
    print("1 - Kolay     (1 - 100)")
    print("2 - Normal    (1 - 200)")
    print("3 - Zor       (1 - 500)")
    print("4 - Hardcore  (1 - 500, sadece 10 deneme)")
    print("5 - Mod seç   (istediğin özel modu kendin seç)")

    secim = sayi_al("Seçimin: ", 1, 5)
    modlar = {
        1: ("Kolay", 100, None, None),
        2: ("Normal", 200, None, None),
        3: ("Zor", 500, None, None),
        4: ("Hardcore", 500, 10, None),
    }
    if secim == 5:
        return "Özel Mod", 200, None, ozel_mod_sec()
    return modlar[secim]


def sans_modu_sec():
    """Şans modu tetiklenirse rastgele bir mod seçer."""
    return random.choice(SANS_MODLARI)


def ozel_mod_sec():
    """Oyuncunun rastgelelik olmadan özel mod seçmesini sağlar."""
    cizgi()
    print("                ÖZEL MODUNU SEÇ")
    for numara, mod_adi in enumerate(SANS_MODLARI, start=1):
        print(f"{numara:2} - {mod_adi}")
    secim = sayi_al("Seçimin: ", 1, len(SANS_MODLARI))
    return SANS_MODLARI[secim - 1]


def sicak_soguk_ipucu(fark):
    if fark == 0:
        return ""
    if fark <= 2:
        return "YANDIN! Sayıya inanılmaz yakınsın!"
    if fark <= 5:
        return "Çok sıcak!"
    if fark <= 10:
        return "Sıcak!"
    if fark <= 25:
        return "Ilık..."
    if fark <= 50:
        return "Serin."
    if fark <= 100:
        return "Soğuk!"
    return "Buz gibi soğuk! Çok uzaktasın."


def asal_mi(sayi):
    """Sayının asal olup olmadığını döndürür."""
    if sayi < 2:
        return False
    for bolen in range(2, int(sayi ** 0.5) + 1):
        if sayi % bolen == 0:
            return False
    return True


def yanik_kopru_baslangici():
    cizgi()
    print("YANIK KÖPRÜ MODU AKTİF!")
    print("Köprüyü geçmek için 1 ile 4 arasında tuttuğum sayıyı bilmelisin.")
    kopru_sayisi = random.randint(1, 4)
    tahmin = tahmin_al(1, 4)

    if tahmin == "q":
        return "cikis"
    if tahmin == "s":
        print("Köprüyü atladın. Ana modunda oynayacaksın.")
        return "atla"

    if tahmin == kopru_sayisi:
        print("Köprüyü geçtin! Seçtiğin modda devam ediyorsun.")
        return True

    print(f"Köprü çöktü! Tutulan sayı: {kopru_sayisi}")
    print("Ceza olarak 1 ile 10.000 arasındaki sayıyı bulmalısın!")
    return False


def oyun_oyna():
    ana_mod, ust_sinir, deneme_limiti, secilen_ozel_mod = ana_mod_sec()
    sans_modu = None

    if secilen_ozel_mod:
        sans_modu = secilen_ozel_mod
        cizgi()
        print(f"SEÇTİĞİN MOD: {sans_modu.upper()}!")
        input("Başlamak için Enter'a bas...")
    elif random.randint(1, 100) <= SANS_MODU_IHTIMALI:
        sans_modu = sans_modu_sec()
        cizgi()
        print(f"ŞANS MODU ÇIKTI: {sans_modu.upper()}!")
        input("Başlamak için Enter'a bas...")

    if sans_modu == "Cehennem":
        mod_adi, ust_sinir, deneme_limiti = "Cehennem", 1000, None
    elif sans_modu == "Melek":
        mod_adi, ust_sinir, deneme_limiti = "Melek", 50, None
    elif sans_modu == "Efsane":
        mod_adi, ust_sinir, deneme_limiti = "Efsane", 10, None
    elif sans_modu == "İmkansız":
        mod_adi, ust_sinir, deneme_limiti = "İmkansız", 1_000_000, None
    elif sans_modu == "Görünmez":
        mod_adi = "Görünmez"
    elif sans_modu == "Sıcak Soğuk":
        mod_adi = "Sıcak Soğuk"
    elif sans_modu == "Ters Dünya":
        mod_adi = "Ters Dünya"
    elif sans_modu == "Mayın Tarlası":
        mod_adi = "Mayın Tarlası"
    elif sans_modu == "Çifte Zafer":
        mod_adi = "Çifte Zafer"
    elif sans_modu == "Kaçan Hedef":
        mod_adi = "Kaçan Hedef"
    elif sans_modu == "Kaymış İpucu":
        mod_adi = "Kaymış İpucu"
    elif sans_modu == "Tek Şans":
        mod_adi, deneme_limiti = "Tek Şans", 1
    elif sans_modu == "Yakın Atış":
        mod_adi = "Yakın Atış"
    elif sans_modu == "Üç Can":
        mod_adi = "Üç Can"
    elif sans_modu == "Yasaklı Rakam":
        mod_adi = "Yasaklı Rakam"
    elif sans_modu == "İki Hedef":
        mod_adi = "İki Hedef"
    elif sans_modu == "Süreye Karşı":
        mod_adi = "Süreye Karşı"
    elif sans_modu == "Asal Avı":
        mod_adi = "Asal Avı"
    elif sans_modu == "Yanık Köprü":
        kopru_sonucu = yanik_kopru_baslangici()
        if kopru_sonucu == "cikis":
            print("Oyun kapatılıyor. Görüşürüz!")
            return False
        if kopru_sonucu == "atla":
            mod_adi = "Yanık Köprü (atlandı)"
        elif kopru_sonucu:
            mod_adi = "Yanık Köprü (başarılı)"
        else:
            mod_adi, ust_sinir, deneme_limiti = "Yanık Köprü (ceza)", 10_000, None
    else:
        mod_adi = ana_mod

    gizli_sayi = random.randint(1, ust_sinir)
    deneme_sayisi = 0
    yanlis_sayisi = 0
    baslangic_zamani = time.monotonic()
    mayinlar = set()
    cift_zafer_bekliyor = False
    bulunan_hedefler = 0
    yasakli_rakam = None

    if sans_modu == "Mayın Tarlası":
        while len(mayinlar) < min(3, ust_sinir - 1):
            mayin = random.randint(1, ust_sinir)
            if mayin != gizli_sayi:
                mayinlar.add(mayin)
    elif sans_modu == "Yasaklı Rakam":
        yasakli_rakam = str(random.randint(0, 9))
    elif sans_modu == "Asal Avı":
        while not asal_mi(gizli_sayi):
            gizli_sayi = random.randint(1, ust_sinir)

    cizgi()
    print(f"MOD: {mod_adi}")
    print(f"1 ile {ust_sinir} arasında bir sayı tuttum.")
    if deneme_limiti:
        print(f"Dikkat: Sadece {deneme_limiti} deneme hakkın var!")
    if sans_modu == "Efsane":
        tur = "çift" if gizli_sayi % 2 == 0 else "tek"
        print(f"Efsane ipucu: Tutulan sayı {tur}.")
    if sans_modu == "Görünmez":
        print("Görünmez mod: İpuçlarının yarısı kaybolacak!")
    if sans_modu == "Sıcak Soğuk":
        print("Sıcak Soğuk mod: Büyük/küçük yerine uzaklık ipucu alacaksın.")
    if sans_modu == "Ters Dünya":
        print("Ters Dünya mod: İpuçları %50 ihtimalle ters söylenecek!")
    if sans_modu == "Mayın Tarlası":
        print("Mayın Tarlası mod: 3 mayınlı sayı var; birini seçersen oyun biter!")
    if sans_modu == "Çifte Zafer":
        print("Çifte Zafer mod: İlk doğru tahminden sonra yeni tutulan sayıyı da bulmalısın.")
    if sans_modu == "Kaçan Hedef":
        print("Kaçan Hedef mod: Her yanlış tahminden sonra sayı yeniden tutulur.")
    if sans_modu == "Kaymış İpucu":
        print("Kaymış İpucu mod: İpucu, tahminin rastgele ±5, ±10 veya ±20 kaymış hâline göre verilir.")
    if sans_modu == "Tek Şans":
        print("Tek Şans mod: Yalnızca bir tahmin yapabilirsin.")
    if sans_modu == "Yakın Atış":
        print("Yakın Atış mod: Sayıya en fazla 3 farkla yaklaşırsan kazanırsın.")
    if sans_modu == "Üç Can":
        print("Üç Can mod: Üç yanlış tahmin yaparsan oyun biter.")
    if sans_modu == "Yasaklı Rakam":
        print(f"Yasaklı Rakam mod: İçinde '{yasakli_rakam}' geçen tahmin yasak; ihlal oyun bitirir!")
    if sans_modu == "İki Hedef":
        print("İki Hedef mod: İlk sayıyı bulunca ikinci, farklı sayıyı da bulmalısın.")
    if sans_modu == "Süreye Karşı":
        print("Süreye Karşı mod: 45 saniye içinde doğru tahmini yapmalısın.")
    if sans_modu == "Asal Avı":
        print("Asal Avı mod: Gizli sayı asal. Yalnızca asal sayıları tahmin edebilirsin.")

    while True:
        if deneme_limiti and deneme_sayisi >= deneme_limiti:
            print(f"\nDeneme hakkın bitti. Sayı {gizli_sayi} idi.")
            return True
        if sans_modu == "Süreye Karşı" and time.monotonic() - baslangic_zamani >= 45:
            print(f"\nSüre doldu. Sayı {gizli_sayi} idi.")
            return True

        tahmin = tahmin_al(1, ust_sinir, gizli_sayi)

        if tahmin == "q":
            print("Oyun kapatılıyor. Görüşürüz!")
            return False
        if tahmin == "s":
            print("Tur atlandı.")
            break

        if sans_modu == "Süreye Karşı" and time.monotonic() - baslangic_zamani >= 45:
            print(f"\nSüre doldu. Sayı {gizli_sayi} idi.")
            return True

        if sans_modu == "Yasaklı Rakam" and yasakli_rakam in str(tahmin):
            print(f"\nYASAKLI RAKAMI KULLANDIN! '{yasakli_rakam}' içeren tahminle oyun bitti.")
            return True

        if sans_modu == "Asal Avı" and not asal_mi(tahmin):
            print("Bu sayı asal değil; Asal Avı'nda yalnızca asal tahmin yapılabilir.")
            continue

        deneme_sayisi += 1

        if sans_modu == "Mayın Tarlası" and tahmin in mayinlar:
            print(f"\nMAYINA BASTIN! Mayınlı sayı {tahmin} idi. Oyun bitti.")
            return True

        if tahmin == gizli_sayi:
            if sans_modu == "İki Hedef" and bulunan_hedefler == 0:
                bulunan_hedefler = 1
                eski_sayi = gizli_sayi
                while gizli_sayi == eski_sayi:
                    gizli_sayi = random.randint(1, ust_sinir)
                print("İlk hedef bulundu! Şimdi ikinci ve farklı hedefi bulmalısın.")
                continue
            if sans_modu == "Çifte Zafer" and not cift_zafer_bekliyor:
                cift_zafer_bekliyor = True
                eski_sayi = gizli_sayi
                while gizli_sayi == eski_sayi:
                    gizli_sayi = random.randint(1, ust_sinir)
                print("İlk isabet! Yeni bir sayı tuttum; zafer için onu da bulmalısın.")
                continue
            print(f"\nTEBRİKLER! {deneme_sayisi} tahminde bildin!")
            return True

        if sans_modu == "Yakın Atış" and abs(gizli_sayi - tahmin) <= 3:
            print(f"\nYAKIN ATIŞ! Sayı {gizli_sayi} idi; sadece {abs(gizli_sayi - tahmin)} farkla kazandın!")
            return True

        yanlis_sayisi += 1
        if sans_modu == "Üç Can":
            kalan_can = 3 - yanlis_sayisi
            if kalan_can <= 0:
                print(f"\nÜç canın da bitti. Sayı {gizli_sayi} idi.")
                return True
            print(f"Kalan canın: {kalan_can}")

        if deneme_limiti:
            kalan = deneme_limiti - deneme_sayisi
            print(f"Kalan deneme hakkın: {kalan}")

        if sans_modu == "Sıcak Soğuk":
            print(sicak_soguk_ipucu(abs(gizli_sayi - tahmin)))
        elif sans_modu == "Ters Dünya":
            ters_ipucu = random.choice([True, False])
            if (tahmin < gizli_sayi) != ters_ipucu:
                print("Daha büyük bir sayı dene.")
            else:
                print("Daha küçük bir sayı dene.")
        elif sans_modu == "Kaymış İpucu":
            kayma = random.choice([-20, -10, -5, 5, 10, 20])
            kaymis_tahmin = tahmin + kayma
            if kaymis_tahmin < gizli_sayi:
                print("Daha büyük bir sayı dene.")
            else:
                print("Daha küçük bir sayı dene.")
        elif sans_modu == "Görünmez" and random.choice([True, False]):
            print("İpucu görünmez oldu...")
        elif tahmin < gizli_sayi:
            print("Daha büyük bir sayı dene.")
        else:
            print("Daha küçük bir sayı dene.")

        if sans_modu == "Kaçan Hedef":
            eski_sayi = gizli_sayi
            while gizli_sayi == eski_sayi:
                gizli_sayi = random.randint(1, ust_sinir)
            print("Hedef kaçtı; artık yeni bir sayı tutuyorum!")


def nasil_oynanir():
    cizgi()
    print("              NASIL OYNANIR?")
    print("Bir ana mod seç ve bilgisayarın tuttuğu sayıyı tahmin et.")
    print(f"Her oyunda %{SANS_MODU_IHTIMALI} ihtimalle rastgele bir şans modu gelir.")
    print("\nŞans modları:")
    print("- Cehennem: 1-1000 aralığı")
    print("- Yanık Köprü: Önce 1-4 sayısını bil; bilemezsen 1-10000 cezası")
    print("- Melek: 1-50 aralığı")
    print("- Efsane: 1-10 aralığı ve tek/çift ipucu")
    print("- İmkansız: 1-1000000 aralığı")
    print("- Görünmez: İpuçlarının %50'si görünmez")
    print("- Sıcak Soğuk: Sayıya yakınlığına göre sıcaklık ipucu")
    print("- Ters Dünya: Büyük/küçük ipuçları %50 ihtimalle ters verilir")
    print("- Mayın Tarlası: 3 mayınlı sayıdan birini seçmek oyunu bitirir")
    print("- Çifte Zafer: İlk doğru tahminden sonra değişen yeni sayıyı da bulmalısın")
    print("- Kaçan Hedef: Her yanlış tahminden sonra gizli sayı değişir")
    print("- Kaymış İpucu: İpucu, tahminin rastgele ±5, ±10 veya ±20 kaymış hâline göre verilir")
    print("- Tek Şans: Sadece bir tahmin hakkın vardır")
    print("- Yakın Atış: Gizli sayıya en fazla 3 farkla yaklaşırsan kazanırsın")
    print("- Üç Can: Üç yanlış tahminden sonra oyun biter")
    print("- Yasaklı Rakam: Belirlenen rakamı içeren tahmin yasaktır")
    print("- İki Hedef: Art arda iki farklı gizli sayıyı bulmalısın")
    print("- Süreye Karşı: 45 saniye içinde sayıyı bulmalısın")
    print("- Asal Avı: Gizli sayı asaldır; sadece asal tahmin yapabilirsin")
    input("\nAna menüye dönmek için Enter'a bas...")


def ana_menu():
    while True:
        cizgi()
        print("          S A Y I   T A H M İ N   O Y U N U")
        tarihi_goster()
        print("1 - Oyuna başla")
        print("2 - Nasıl oynanır?")
        print("3 - Çıkış")

        secim = sayi_al("Seçimin: ", 1, 3)

        if secim == 1:
            devam = oyun_oyna()
            if devam is False:
                break
            input("\nAna menüye dönmek için Enter'a bas...")
        elif secim == 2:
            nasil_oynanir()
        else:
            print("Oynadığın için teşekkürler. Görüşürüz!")
            break


if __name__ == "__main__":
    ana_menu()
